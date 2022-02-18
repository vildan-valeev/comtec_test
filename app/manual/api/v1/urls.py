from django.urls import path, register_converter

from manual.api.v1.views import ManualList, ManualListAsOfDate, ItemList, ItemListByVersion
from manual.serices.url_converter import DateConverter, VersionConverter

register_converter(DateConverter, 'dd-mm-yyyy')
register_converter(VersionConverter, 'vv')

urlpatterns = [
    path('manual/', ManualList.as_view()),
    path('manual/current/<dd-mm-yyyy:date>/', ManualListAsOfDate.as_view()),
    # path('item/', ItemCreateList.as_view()),
    path('item/<uuid:id>/', ItemList.as_view()),
    path('item/<uuid:id>/<vv:version>/', ItemListByVersion.as_view()),
]
