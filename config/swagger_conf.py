from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
      title="Game API",
      default_version='v1',
      description="Build in simple game | API",
      terms_of_service="None",
      contact=openapi.Contact(email="mehmonov.husniddin1@gmail.com"),
      license=openapi.License(name="No License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)