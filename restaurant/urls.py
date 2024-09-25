from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

# Create a router object
router = DefaultRouter()

# Register the 'tables' route with the BookingViewSet class
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name="home"),
    path('menu/', views.MenuItemsView.as_view(), name='menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='menu-item'),
    path('booking/', include(router.urls)),
]
