from datetime import datetime

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from manual.api.v1.serializers import ManualListSerializer, ManualListAsOfDateSerializer, ItemListSerializer
from manual.generics.item_views import CustomItemAPIView
from manual.models import Manual, Item
from manual.serices.check_items_in_db import having_items


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


class ItemCurrentList(ListAPIView):
    """    """
    serializer_class = ItemListSerializer

    def get_queryset(self, *args, **kwargs):
        """ """
        # TODO: вынести в services
        # по id базового справочника и дате версии находим актуальные - на текущий день
        return Item.objects.filter(manual__manual_base_id=self.kwargs['id'], manual__enable_date__lte=datetime.now())


class ItemListByVersion(ListAPIView):
    """    """
    serializer_class = ItemListSerializer

    def get_queryset(self, *args, **kwargs):
        """ """
        print(self.kwargs)
        # TODO: вынести в services
        date = Manual.objects.filter(manual_base_id=self.kwargs['id'],
                                     version=self.kwargs['version']).first().enable_date
        return Item.objects.filter(manual__manual_base_id=self.kwargs['id'], manual__enable_date__lte=date)


test = [
    {
        "code": "string",
        "summary": "string",
        "manual": "35c55e7f-8d6d-46ff-bc84-64c4c6e22a3b"
    },
    {
        "code": "string",
        "summary": "string",
        "manual": "35c55e7f-8d6d-46ff-bc84-64c4c6e22a3b"
    }
]


class ValidateItems(CustomItemAPIView):
    """Проверка есть ли элементы в справочнике
    [
        {
            "code": "string",
            "summary": "string",
            "manual": "35c55e7f-8d6d-46ff-bc84-64c4c6e22a3b"
        },
        {
            "code": "string",
            "summary": "string",
            "manual": "35c55e7f-8d6d-46ff-bc84-64c4c6e22a3b"
        }
    ]

    """
    # TODO: добавить пример в схему
    serializer_class = ItemListSerializer

    @swagger_auto_schema(responses={status.HTTP_200_OK: 'ОК',
                                    status.HTTP_204_NO_CONTENT: 'Нет элемента(ов) в справочнике',
                                    status.HTTP_400_BAD_REQUEST: 'Error text'},
                         )
    def post(self, request, *args, **kwargs):
        serializer = ItemListSerializer(data=request.data, many=True)
        if serializer.is_valid():
            print(serializer.validated_data)
            if having_items(serializer.validated_data):
                return Response('ОК', status=status.HTTP_200_OK)
            return Response('Нет элемента(ов) в справочнике', status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ValidateItemByVersion(APIView):

    def post(self):
        return Response('ok', status=status.HTTP_200_OK)
