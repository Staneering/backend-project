from django.shortcuts import render
import requests
from datetime import datetime, timezone

# Create your views here.
from django.http import JsonResponse

def hello_view(request):
    data = {
        "message": "Hello from Django backend!"
    }
    return JsonResponse(data)

def profile_view(request):
    try:
        profile = {
            "name": "Ikegbo Stanley Ogochukwu",
            "email": "stacymacbrains@gmail.com",
            "github": "https://github.com/Staneering",
            "bio": "Backend developer passionate about APIs and Django."
        }

        # Fetch dynamic cat fact
        response = requests.get("https://catfact.ninja/fact")
        response.raise_for_status()
        cat_data = response.json()

        data = {
            "status": "success",
            "user": profile,
            "fact": cat_data.get("fact", "No cat fact available right now."),
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
    except Exception as e:
        data = {
            "error": "Failed to fetch profile or cat fact.",
            "details": str(e)
        }



    return JsonResponse(data)