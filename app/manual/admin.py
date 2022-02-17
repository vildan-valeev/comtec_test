from django.contrib import admin
from django.contrib.auth.models import Group


from manual.models import ManualVersion, Manual, Item
from manual.serices.item_list_filter import ItemsIncomingToVersionFilter


class ManualVersionTabular(admin.TabularInline):
    model = ManualVersion
    # max_num = 0
    extra = 0
    # readonly_fields = ['version']


class ManualAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'short_name']
    readonly_fields = ['id']
    inlines = [ManualVersionTabular, ]


class ManualVersionAdmin(admin.ModelAdmin):
    list_display = ['id', 'manual', 'version', 'enable_date']


class ItemAdmin(admin.ModelAdmin):
    # version, manual подтягиваются из методов в Item - не путать с полями ManualVersion
    list_display = ['id', 'code', 'summary', 'manual', 'version']
    readonly_fields = ['manual', 'version']
    list_filter = ['manual_version', 'manual_version__manual', ItemsIncomingToVersionFilter]
    date_hierarchy = 'manual_version__enable_date'

admin.site.register(Item, ItemAdmin)
admin.site.register(Manual, ManualAdmin)
admin.site.unregister(Group)

# можно отключить, версии нельзя удалить пока есть элемент справочника
# удаление самой версии только из справочника
admin.site.register(ManualVersion, ManualVersionAdmin)
