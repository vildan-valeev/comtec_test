from rest_framework.generics import GenericAPIView


class CustomItemAPIView(GenericAPIView):
    """ """
    def get_serializer(self, *args, **kwargs):
        """ if an array is passed, set serializer to many """
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super().get_serializer(*args, **kwargs)
