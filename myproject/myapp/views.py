from rest_framework import viewsets
from rest_framework import filters as search
from django_filters import rest_framework as filters
from .models import Client
from .serializers import ClientSerializer
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.http import JsonResponse

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
   
class AddTicketView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    def post(self, request, client_id):
        try:
            client = Client.objects.get(id=client_id)
            ticket = json.loads(request.body)
            client.tickets.append(ticket)
            client.save()
            return JsonResponse({'message': 'Ticket added successfully!'})
        except Client.DoesNotExist:
            return JsonResponse({'error': 'Client not found'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        
class GetTicketsView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    def get(self, request, client_id):
        try:
            client = Client.objects.get(id=client_id)
            return JsonResponse(client.tickets, safe=False)
        except Client.DoesNotExist:
            return JsonResponse({'error': 'Client not found'}, status=404)