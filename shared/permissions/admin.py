from rest_framework.permissions import BasePermission

from core.models import User

from accountio.choices import VendorUserRole


class IsAdminOwner(BasePermission):
    def has_permission(self, request, view):
        try:
            user: User = request.user
            admin_user = user.adminuser

            return admin_user and admin_user.role == VendorUserRole.OWNER
        except:
            return False


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        try:
            user: User = request.user
            admin_user = user.adminuser

            return admin_user and admin_user.role in {
                VendorUserRole.OWNER,
                VendorUserRole.ADMIN,
            }
        except:
            return False


class IsAdminStaff(BasePermission):
    def has_permission(self, request, view):
        try:
            user: User = request.user
            admin_user = user.adminuser

            return admin_user and admin_user.role in {
                VendorUserRole.OWNER,
                VendorUserRole.ADMIN,
                VendorUserRole.STAFF,
            }
        except:
            return False


class IsSuperuserStaff(BasePermission):
    def has_permission(self, request, view):
        subdomain, hostname, _ = get_and_split_x_domain()
        try:
            user: User = request.user
            admin_user = user.adminuser_set.filter(hostname=hostname).first()

            return admin_user and admin_user.role in {
                AdminRoleChoices.SUPERUSER,
                AdminRoleChoices.OWNER,
                AdminRoleChoices.ADMIN,
                AdminRoleChoices.HR,
                AdminRoleChoices.STAFF,
            }
        except:
            return False


class IsSuperuserDataEntry(BasePermission):
    def has_permission(self, request, view):
        subdomain, hostname, _ = get_and_split_x_domain()
        try:
            user: User = request.user
            admin_user = user.adminuser_set.filter(hostname=hostname).first()

            return admin_user and admin_user.role in {
                AdminRoleChoices.SUPERUSER,
                AdminRoleChoices.OWNER,
                AdminRoleChoices.ADMIN,
                AdminRoleChoices.HR,
                AdminRoleChoices.STAFF,
                AdminRoleChoices.DATA_ENTRY,
            }
        except:
            return False
