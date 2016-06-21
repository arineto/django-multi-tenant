from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from .exceptions import IncorrectTenantException
from .exceptions import InactiveUserException
from .exceptions import UserDoesNotExistException


def login(request, username, password, tenant):
    if tenant.has_user(username):
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                django_login(request, user)
            raise InactiveUserException('This user is not active.')
        raise UserDoesNotExistException('This user does not exist.')
    raise IncorrectTenantException('Incorrect Tenant.')
