from rest_framework.routers import DefaultRouter
from accounts.api.v1 import views
from django.urls import path


app_name = 'accounts-api'
router = DefaultRouter()
router.register('account', views.UserView, basename='account')
urlpatterns = router.urls

# urlpatterns = [
#     path('account/', views.UserView.as_view({'get': 'list', 'post': 'create'}), name='account-list')
# ]
