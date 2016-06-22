from .exceptions import IncorrectTenantException


def belongs_to_tenant(username, tenant):
    """
    This function checks if the user belongs to the given Tenant.
    """
    user_exists = tenant.users.filter(username=username).exists()
    if not user_exists:
        raise IncorrectTenantException()
