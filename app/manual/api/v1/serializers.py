from rest_framework import serializers

from manual.models import Manual, Item


class ManualListSerializer(serializers.ModelSerializer):
    """
    Сериализатор Справочника.
    С добавлением полей от базового справочника
    """
    id = serializers.CharField(read_only=True, source="manual_base.id")
    # id_version = serializers.IntegerField(read_only=True, source="id")
    name = serializers.CharField(read_only=True, source="manual_base.name")
    short_name = serializers.CharField(read_only=True, source="manual_base.short_name")

    class Meta:
        model = Manual
        exclude = ['manual_base', ]


class ManualListAsOfDateSerializer(ManualListSerializer):
    """  """
    pass


class ItemSerializer(serializers.ModelSerializer):
    """Базовый Сериализатор Элемент справочника"""

    class Meta:
        model = Item
        exclude = ['id']


class ItemListSerializer(ItemSerializer):
    """Сериализатор Элемент справочника"""
    manual = serializers.UUIDField(read_only=True, source="manual.manual_base.id")


class ItemValidateSerializer(ItemSerializer):
    """Сериализатор Элемент справочника"""
    manual = serializers.UUIDField(source="manual.manual_base.id")


