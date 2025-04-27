import random


def generate_order_id(self):
    from orderio.models import Order

    random_number = random.randint(10000000, 99999999)

    order_id = "#" + str(random_number)

    if Order.objects.filter(order_id=order_id).exists():
        return generate_order_id(self)
    else:
        return order_id
