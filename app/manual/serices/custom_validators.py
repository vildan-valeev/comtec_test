from django.core.exceptions import ValidationError


def validate_version(value):
    print(value)
    # if value % 2 != 0:
    #     raise ValidationError('%(value)s is not an even number', params={'value': value},)
