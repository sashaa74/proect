from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.views import View
import os

class FlightSearchView(View):
    def get(self, request):
        url = "https://api.travelpayouts.com/aviasales/v3/prices_for_dates"
        params = {
            'currency': request.GET.get('currency', 'rub'),
            'origin': request.GET.get('origin'),
            'destination': request.GET.get('destination'),
            'departure_at': request.GET.get('departure_at'),
            'return_at': request.GET.get('return_at'),
            'one_way': request.GET.get('one_way', 'true'),
            'direct': request.GET.get('direct', 'false'),
            'market': request.GET.get('market', 'ru'),
            'limit': request.GET.get('limit', 30),
            'page': request.GET.get('page', 1),
            'sorting': request.GET.get('sorting', 'price'),
            'unique': request.GET.get('unique', 'false'),
            'token': '299584abf4662095d71ea40fa970db6d'
        }

        response = requests.get(url, params=params)
        
        try:
            data = response.json()
        except ValueError:
            return JsonResponse({'error': 'Invalid response from API', 'response_text': response.text}, status=500)
        
        return JsonResponse(data, safe=False)
