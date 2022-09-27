from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_roles(chief, employee):
    diff = chief.role_level - employee.role_level
    if diff != 1:
        raise ValidationError(
            _('%(value)s cannot have chief - employee relationships'),
            params={'value': (chief, employee)}
        )