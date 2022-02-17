from django.contrib import admin
from django.contrib.auth.models import Group

from manual.models import Manual, ManualBase, Item
from manual.serices.item_list_filter import ItemsIncomingToVersionFilter


class ManualTabular(admin.TabularInline):
    model = Manual
    # max_num = 0
    extra = 0
    # readonly_fields = ['version']


class ManualBaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'short_name']
    readonly_fields = ['id']
    inlines = [ManualTabular, ]


class ManualAdmin(admin.ModelAdmin):
    list_display = ['id', 'manual_base', 'version', 'enable_date']
    readonly_fields = ['name', 'short_name', 'description']


class ItemAdmin(admin.ModelAdmin):
    # manual_version, manual_name подтягиваются из методов в Item - не путать с полями ManualVersion
    list_display = ['id', 'code', 'summary', 'manual_name', 'manual_version']
    readonly_fields = ['manual_name', 'manual_version', 'manual_date']
    list_filter = ['manual', 'manual__manual_base', ItemsIncomingToVersionFilter]
    date_hierarchy = 'manual__enable_date'
    actions_on_bottom = True


admin.site.register(Item, ItemAdmin)
admin.site.register(ManualBase, ManualBaseAdmin)
admin.site.register(Manual, ManualAdmin)
admin.site.unregister(Group)
