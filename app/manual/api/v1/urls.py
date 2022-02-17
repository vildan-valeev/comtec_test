from django.urls import path, register_converter

from manual.api.v1.views import ManualList, ManualListAsOfDate
from manual.serices.url_converter import DateConverter

register_converter(DateConverter, 'dd-mm-yyyy')

urlpatterns = [
    path('manual/', ManualList.as_view()),
    path('manual/current/<dd-mm-yyyy:date>/', ManualListAsOfDate.as_view()),
    # path('item/', ItemCreateList.as_view()),
    # path('item/<int:pk>/', ItemDetail.as_view()),
]
