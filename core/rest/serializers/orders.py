from django.db import transaction
from django.utils import timezone

from rest_framework import serializers

from orderio.choices import OrderType
from orderio.models import Order, OrderItems

from productio.models import Product
from productio.rest.serializers.products import PublicProductSerializer


class UserProductItemsSerializer(serializers.Serializer):
    product_uids = serializers.SlugRelatedField(
        queryset=Product.objects.all(),
        slug_field="uid",
        write_only=True,
        required=True,
    )
    quantity = serializers.IntegerField(default=1)


class UserOrderListSerializer(serializers.ModelSerializer):
    products = PublicProductSerializer(many=True, read_only=True)
    selected_products = UserProductItemsSerializer(
        many=True, write_only=True, required=True
    )

    class Meta:
        model = Order
        fields = [
            "uid",
            "created_at",
            "updated_at",
            "order_id",
            "address",
            "products",
            "selected_products",
            "status",
            "total_price",
        ]
        read_only_fields = [
            "uid",
            "created_at",
            "updated_at",
            "order_id",
            "status",
            "total_price",
        ]

    @transaction.atomic
    def create(self, validated_data):
        user = self.context["request"].user

        # Create Order
        order = Order.objects.create(
            user=user,
            status=OrderType.ORDER_PLACED,
            is_ordered=True,
            address=validated_data.get("address", ""),
        )

        selected_products = validated_data.pop("selected_products", [])

        order_items = []
        total_price = 0
        for product in selected_products:
            item = OrderItems(
                order=order,
                product=product.get("product_uids"),
                quantity=product.get("quantity"),
                total_product_price=product.get("product_uids").unit_price
                * product.get("quantity"),
                updated_at=timezone.now(),
            )
            order_items.append(item)
            total_price += product.get("product_uids").unit_price * product.get(
                "quantity"
            )

        OrderItems.objects.bulk_create(order_items)

        order.total_price = total_price
        order.save_dirty_fields()

        return validated_data
