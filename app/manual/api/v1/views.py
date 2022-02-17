from rest_framework.generics import ListAPIView, RetrieveAPIView

from manual.api.v1.serializers import ManualListSerializer, ManualListAsOfDateSerializer
from manual.models import Manual


class ManualList(ListAPIView):
    queryset = Manual.objects.all()
    serializer_class = ManualListSerializer

    # def get_queryset(self):
    #     pass


class ManualListAsOfDate(ListAPIView):
    # queryset = Manual.objects.all()
    serializer_class = ManualListAsOfDateSerializer

    def get_queryset(self, *args, **kwargs):
        print(self.kwargs['date'])
        return Manual.objects.all()
