from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter
from .views import RoomViewSet, QuestionViewSet, OptionViewSet



urlpatterns = [
    re_path(r'^rooms/', RoomViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    re_path(r'^rooms/(?P<pk>\d+)/$', RoomViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),
    re_path(r'^rooms/(?P<room_pk>\d+)/questions/', QuestionViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    re_path(r'^questions/(?P<question_pk>\d+)/options/', OptionViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
]