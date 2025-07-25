from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserForm
from .models import Place, Hotel
import requests
from django.http import JsonResponse

# Blynk API URL


def register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! You can log in now.")
            return redirect('/login')
    return render(request, "register.html", {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def search(request):
    if request.method == 'POST':
        destination = request.POST.get('destination')
        places = Place.objects.filter(name__icontains=destination)
        return render(request, 'search_results.html', {'places': places, 'destination': destination})
    return render(request, 'home.html')

def hotel(request):
    if request.method == 'POST':
        hotel_query = request.POST.get('hotel', '')
        hotel_names = Hotel.objects.filter(hotel_name__icontains=hotel_query)
        return render(request, 'hotel.html', {'hotel_names': hotel_names, 'hotel': hotel_query})
    return render(request, 'home.html')

def home(request):
    return render(request, "home.html")
"""
import requests

def get_blynk_value(pin, auth_token):
    url = f"https://blynk.cloud/external/api/get?token={auth_token}&pin={pin}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print(f"Data from {pin}: {data}")  # Debugging output
        
        if isinstance(data, list) and data:
            return data[0]
        elif isinstance(data, int):
            return data
    except requests.RequestException as e:
        print(f"Request failed: {e}")
    except ValueError as e:
        print(f"Error parsing JSON: {e}")
    
    return None
#BLYNK_API_URL = 'https://blynk.cloud/external/api/update?token=1t5QFOEQmg607WafpM03E5Fy78xcVUXd&V0'
auth_token = "1t5QFOEQmg607WafpM03E5Fy78xcVUXd"

# Example usage
V0_value = get_blynk_value("V0", auth_token)
print(f"V0: {V0_value}")

def display_sensor_data(request):
    TEMP_VPIN = "V0"  # Replace with actual pin
    auth_token = "1t5QFOEQmg607WafpM03E5Fy78xcVUXd"

    notification = get_blynk_value(TEMP_VPIN, auth_token)

    context = {}  # Ensure context is always defined

    if notification == 1:
        context['note'] = "Alert: Child Missing! Login to Find!!!"
        print(context)

    return render(request, 'home.html', context)

"""