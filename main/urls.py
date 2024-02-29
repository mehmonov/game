from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import RoomViewSet, OptionViewSet, QuestionViewSet

router = DefaultRouter()
router.register(r'rooms', RoomViewSet, basename='room')
router.register(r'options', OptionViewSet, basename='option')
router.register(r'questions', QuestionViewSet, basename='question')

urlpatterns = [
    path('', include(router.urls)),
]