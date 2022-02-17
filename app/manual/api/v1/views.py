from rest_framework.generics import ListAPIView, RetrieveAPIView


class ManualList(ListAPIView):
    serializer_class = ...

    def get_queryset(self):
        pass


class ManualInstanceDetail(RetrieveAPIView):
    serializer_class = ...
    queryset = ...

