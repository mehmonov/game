from django.urls import path
from .views import UserCreate, UserDetail, UserList
urlpatterns = [
  path('users', UserList.as_view(), name='usermain'),
  path('userdetail/<int:pk>/', UserDetail.as_view(), name='userdetail'),
  
  path('createuser', UserCreate.as_view(), name='usercreate'),
]
