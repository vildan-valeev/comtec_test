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
    """

    """
    pass


class ItemListSerializer(serializers.ModelSerializer):
    """Сериализатор Элемент справочника"""

    class Meta:
        model = Item
        fields = '__all__'
