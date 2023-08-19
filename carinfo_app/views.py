from django.shortcuts import render
from django.http import JsonResponse
import requests

def index(request):
    return render(request, 'carinfo_app/index.html')

def get_car_info(request):
    model = request.GET.get('model', '')
    limit = int(request.GET.get('resultLimit', 5))  # Default limit is 5

    api_url = f'https://api.api-ninjas.com/v1/cars?limit={limit}&model={model}'
    response = requests.get(api_url, headers={'X-Api-Key': 'T3ahI7l0grXOUzogXcbXag==lrNS2CC4eJNavt30'})

    if response.status_code == requests.codes.ok:
        car_data = response.json()
    else:
        car_data = []

    return render(request, 'carinfo_app/car_details.html', {'car_data': car_data, 'default_limit': limit, 'default_model': model})

