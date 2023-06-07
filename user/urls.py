from django.urls import path, include

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls'))
]

# ---------- Router ----------
from rest_framework.routers import DefaultRouter
from .views import UserCreateView, UserView
router = DefaultRouter()
router.register('create', UserCreateView)
router.register('', UserView)
urlpatterns += router.urls