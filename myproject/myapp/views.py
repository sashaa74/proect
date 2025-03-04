from rest_framework import viewsets
from rest_framework import filters as search
from django_filters import rest_framework as filters
from .models import Client
from .serializers import ClientSerializer

class ClientFilter(filters.FilterSet):
    class Meta:
        model = Client
        fields = ['date_of_birth']
        
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = (filters.DjangoFilterBackend, search.SearchFilter)
    filterset_class = ClientFilter
    search_fields = ['first_name', 'last_name', 'email', 'address']