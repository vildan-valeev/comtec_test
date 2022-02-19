from rest_framework.generics import GenericAPIView


class CustomItemAPIView(GenericAPIView):
    """ Добавляем атрибут many = True в сериализатор если передан список """
    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super().get_serializer(*args, **kwargs)
