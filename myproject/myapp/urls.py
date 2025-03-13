from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet
from .views import AddTicketView, GetTicketsView

router = DefaultRouter()
router.register(r'clients', ClientViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('clients/<int:client_id>/add_ticket/', AddTicketView.as_view(), name='add-ticket'),
    path('clients/<int:client_id>/tickets/', GetTicketsView.as_view(), name='get-tickets'),
]