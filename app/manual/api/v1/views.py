from datetime import datetime

from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from manual.api.v1.doc.schemas import validate_items_response_schema
from manual.api.v1.serializers import ManualListSerializer, ManualListAsOfDateSerializer, ItemListSerializer, \
    ItemValidateSerializer
from manual.generics.item_views import CustomItemAPIView
from manual.models import Manual, Item
from manual.serices.check_items_in_db import having_items
from manual.serices.querysets import manual_list_date, item_current_list, item_list_by_version

from src.settings import CUSTOM_RESPONSES


class ManualList(ListAPIView):
    """ Получение списка справочников"""
    queryset = Manual.objects.all()
    serializer_class = ManualListSerializer

    @swagger_auto_schema(operation_summary=__doc__)  # Убрать метод, если doc длинный. Вставить другой str, если разные,
    def get(self, request, *args, **kwargs):
        return super().get(self, request, *args, **kwargs)


class ManualListAsOfDate(ListAPIView):
    """  Получение списка справочников, актуальных на указанную дату

    15-01-2022 - example
    """
    serializer_class = ManualListAsOfDateSerializer

    @swagger_auto_schema(operation_summary=__doc__)  # Убрать метод, если doc длинный. Вставить другой str, если разные,
    def get(self, request, *args, **kwargs):
        return super().get(self, request, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        """ Получаем qs - Справочники отфильтрованные по указанной дате """
        return manual_list_date(*args, **kwargs)


class ItemCurrentList(ListAPIView):
    """  Получение элементов заданного справочника текущей версии  """
    serializer_class = ItemListSerializer

    @swagger_auto_schema(operation_summary=__doc__)  # Убрать метод, если doc длинный. Вставить другой str, если разные,
    def get(self, request, *args, **kwargs):
        return super().get(self, request, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        """ """
        return item_current_list(*args, **kwargs)


class ItemListByVersion(ListAPIView):
    """  Получение элементов заданного справочника указанной версии

    00.01 example version
    """
    serializer_class = ItemListSerializer

    @swagger_auto_schema(operation_summary=__doc__)  # Убрать метод, если doc длинный. Вставить другой str, если разные,
    def get(self, request, *args, **kwargs):
        return super().get(self, request, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        """ """
        return item_list_by_version(*args, **kwargs)


class ValidateItems(CustomItemAPIView):
    """ Валидация элементов заданного справочника текущей версии """
    serializer_class = ItemValidateSerializer

    @swagger_auto_schema(
        request_body=ItemValidateSerializer(many=True),
        responses=validate_items_response_schema,
        operation_summary=__doc__
    )
    def post(self, request, *args, **kwargs):
        serializer = ItemValidateSerializer(data=request.data, many=True)
        if serializer.is_valid():
            if having_items(serializer.data):
                return Response(CUSTOM_RESPONSES[0], status=status.HTTP_200_OK)
            return Response(CUSTOM_RESPONSES[1], status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ValidateItemByVersion(CustomItemAPIView):
    """ Валидация элемента заданного справочника по указанной версии"""
    serializer_class = ItemValidateSerializer

    @swagger_auto_schema(responses=validate_items_response_schema, operation_summary=__doc__)
    def post(self, request, *args, **kwargs):
        serializer = ItemValidateSerializer(data=request.data)
        if serializer.is_valid():
            # [serializer.data] - передается один элемент вложенный в list,т.к. having_item - общая функция проверки
            if having_items([serializer.data], version=self.kwargs['version']):
                return Response(CUSTOM_RESPONSES[0], status=status.HTTP_200_OK)
            return Response(CUSTOM_RESPONSES[1], status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
