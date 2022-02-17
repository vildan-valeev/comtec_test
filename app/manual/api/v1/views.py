from rest_framework.generics import ListAPIView, RetrieveAPIView

from manual.api.v1.serializers import ManualSerializer
from manual.models import Manual


class ManualList(ListAPIView):
    queryset = Manual.objects.all()
    serializer_class = ManualSerializer

    # def get_queryset(self):
    #     pass


class ManualInstanceDetail(RetrieveAPIView):
    serializer_class = ...
    queryset = ...

