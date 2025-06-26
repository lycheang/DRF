from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccountViewSet

router = DefaultRouter()
router.register(r'student', AccountViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]