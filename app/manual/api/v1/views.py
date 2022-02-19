from datetime import datetime

from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from manual.api.v1.serializers import ManualListSerializer, ManualListAsOfDateSerializer, ItemListSerializer, \
    ItemValidateSerializer
from manual.generics.item_views import CustomItemAPIView
from manual.models import Manual, Item
from manual.serices.check_items_in_db import having_items


class ManualList(ListAPIView):
    """ Получение списка справочников"""
    queryset = Manual.objects.all()
    serializer_class = ManualListSerializer


class ManualListAsOfDate(ListAPIView):
    """  Получение списка справочников, актуальных на указанную дату """
    serializer_class = ManualListAsOfDateSerializer

    def get_queryset(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        :return:
        """
        return Manual.objects.filter(enable_date__lte=self.kwargs['date'])


class ItemCurrentList(ListAPIView):
    """  Получение элементов заданного справочника текущей версии  """
    serializer_class = ItemListSerializer

    def get_queryset(self, *args, **kwargs):
        """ """
        # TODO: вынести в services
        # по id базового справочника и дате версии находим актуальные - на текущий день
        return Item.objects.filter(manual__manual_base_id=self.kwargs['id'], manual__enable_date__lte=datetime.now())


class ItemListByVersion(ListAPIView):
    """  Получение элементов заданного справочника указанной версии  """
    serializer_class = ItemListSerializer

    def get_queryset(self, *args, **kwargs):
        """ """
        print(self.kwargs)
        # TODO: вынести в services
        date = Manual.objects.filter(manual_base_id=self.kwargs['id'],
                                     version=self.kwargs['version']).first().enable_date
        return Item.objects.filter(manual__manual_base_id=self.kwargs['id'], manual__enable_date__lte=date)


class ValidateItems(CustomItemAPIView):
    # TODO: добавить пример в схему swagger
    """ Валидация элементов заданного справочника текущей версии
    [
        {
            "code": "469",
            "summary": "Summary text 1",
            "manual": "35c55e7f-8d6d-46ff-bc84-64c4c6e22a3b"
        },
        {
            "code": "468",
            "summary": "Summary text 2",
            "manual": "35c55e7f-8d6d-46ff-bc84-64c4c6e22a3b"
        }
    ]

    """

    serializer_class = ItemValidateSerializer

    @swagger_auto_schema(responses={status.HTTP_200_OK: 'ОК',
                                    status.HTTP_204_NO_CONTENT: 'Нет элемента(ов) в справочнике',
                                    status.HTTP_400_BAD_REQUEST: 'Error text'},
                         )
    def post(self, request, *args, **kwargs):
        serializer = ItemValidateSerializer(data=request.data, many=True)
        if serializer.is_valid():
            print(serializer.data)
            if having_items(serializer.data):
                return Response({'result': 'ОК'}, status=status.HTTP_200_OK)
            return Response({'result': 'Нет элемента(ов) в справочнике'}, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ValidateItemByVersion(APIView):
    serializer_class = ItemValidateSerializer

    @swagger_auto_schema(responses={status.HTTP_200_OK: 'ОК',
                                    status.HTTP_204_NO_CONTENT: 'Нет элемента(ов) в справочнике для заданной версии',
                                    status.HTTP_400_BAD_REQUEST: 'Error text'},
                         )
    def post(self, request, *args, **kwargs):
        serializer = ItemValidateSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data)
            # [serializer.data] - передается один элемент вложенный в list,т.к. having_item - общая функция проверки
            if having_items([serializer.data], version=self.kwargs['version']):
                return Response({'result': 'ОК'}, status=status.HTTP_200_OK)
            return Response({'result': 'Нет элемента(ов) в справочнике для заданной версии'}, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
