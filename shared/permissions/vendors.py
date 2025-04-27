from rest_framework.permissions import BasePermission

from accountio.models import Vendor, VendorUser


class IsVendor(BasePermission):
    """
    Owner, Admin, HR, HR Member or job evaluator  can access this staff permission
    """

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        vendor_uid = view.kwargs.get("vendor_uid")
        try:
            vendor = Vendor.objects.get(uid=vendor_uid)
        except:
            return False

        if VendorUser.objects.filter(vendor=vendor, user=request.user).exists():
            return True
        return False
