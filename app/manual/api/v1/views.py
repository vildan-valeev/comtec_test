from rest_framework.generics import ListAPIView, RetrieveAPIView

from manual.api.v1.serializers import ManualListSerializer, ManualListAsOfDateSerializer, ItemListSerializer
from manual.models import Manual, Item
from manual.serices.near_date import near_date


class ManualList(ListAPIView):
    """

    """
    queryset = Manual.objects.all()
    serializer_class = ManualListSerializer


class ManualListAsOfDate(ListAPIView):
    """

    """
    serializer_class = ManualListAsOfDateSerializer

    def get_queryset(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        :return:
        """
        return Manual.objects.filter(enable_date__lte=self.kwargs['date'])


class ItemList(ListAPIView):
    """    """
    serializer_class = ItemListSerializer

    def get_queryset(self, *args, **kwargs):
        """ """
        # по id базового справочника находим актуальный справочник - дату (до которой все элементы считаются актуальные)
        date = near_date(self.kwargs['id'])
        return Item.objects.filter(manual__manual_base_id=self.kwargs['id'], manual__enable_date__lte=date)


class ItemListByVersion(ListAPIView):
    """    """
    serializer_class = ItemListSerializer

    def get_queryset(self, *args, **kwargs):
        """ """
        print(self.kwargs)
        # TODO: edit
        return Item.objects.all()
