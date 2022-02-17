from django.urls import path

from manual.api.v1.views import ManualList

urlpatterns = [
    path('manual/', ManualList.as_view()),
    path('manual/current/<fds>', ManualList.as_view()),
    # path('item/', ItemCreateList.as_view()),
    # path('item/<int:pk>/', ItemDetail.as_view()),
]
