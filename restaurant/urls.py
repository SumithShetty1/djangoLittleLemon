from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

# Create a router object
router = DefaultRouter()

# Register the 'tables' route with the BookingViewSet class
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('menu/', views.MenuItemsView.as_view(), name='menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='menu-item'),
    path('booking/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
]
