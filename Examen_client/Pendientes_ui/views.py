from django.shortcuts import render
import requests

API_URL_BASE = 'http://localhost:8000/api/pendientes/'

def home(request):
    return render(request, 'home.html')

def pendientes_ids(request):
    response = requests.get(f'{API_URL_BASE}ids/')
    pendientes = response.json()
    return render(request, 'pendientes_list.html', {'pendientes': pendientes, 'type': 'IDs'})

def pendientes_ids_titles(request):
    response = requests.get(f'{API_URL_BASE}ids_titles/')
    pendientes = response.json()
    return render(request, 'pendientes_list.html', {'pendientes': pendientes, 'type': 'IDs and Titles'})

def pendientes_unresolved(request):
    response = requests.get(f'{API_URL_BASE}unresolved/')
    pendientes = response.json()
    return render(request, 'pendientes_list.html', {'pendientes': pendientes, 'type': 'Unresolved'})

def pendientes_resolved(request):
    response = requests.get(f'{API_URL_BASE}resolved/')
    pendientes = response.json()
    return render(request, 'pendientes_list.html', {'pendientes': pendientes, 'type': 'Resolved'})

def pendientes_ids_userids(request):
    response = requests.get(f'{API_URL_BASE}ids_userids/')
    pendientes = response.json()
    return render(request, 'pendientes_list.html', {'pendientes': pendientes, 'type': 'IDs and UserIDs'})

def pendientes_resolved_userids(request):
    response = requests.get(f'{API_URL_BASE}resolved_userids/')
    pendientes = response.json()
    return render(request, 'pendientes_list.html', {'pendientes': pendientes, 'type': 'Resolved UserIDs'})

def pendientes_unresolved_userids(request):
    response = requests.get(f'{API_URL_BASE}unresolved_userids/')
    pendientes = response.json()
    return render(request, 'pendientes_list.html', {'pendientes': pendientes, 'type': 'Unresolved UserIDs'})

# Create your views here.
