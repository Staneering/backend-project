from django.shortcuts import render
import requests
from datetime import datetime, timezone

# Create your views here.
from django.http import JsonResponse

"""def hello_view(request):
    data = {
        "message": "Hello from Django backend!"
    }
    return JsonResponse(data)
    """

def profile_view(request):
    profile = {
        "name": "Ikegbo Stanley Ogochukwu",
        "email": "stacymacbrains@gmail.com",
        "stack": "Python/Django",
        #"github": "https://github.com/Staneering",
        #"bio": "Backend developer passionate about APIs and Django."
        }
    
    cat_fact = "Could not fetch a cat fact right now. Please try again later."
    try:
        # Fetch dynamic cat fact
        response = requests.get("https://catfact.ninja/fact", timeout = 5)
        response.raise_for_status()
        cat_data = response.json()
        cat_fact = cat_data.get("fact", cat_fact)
        status = "success"
    except requests.exceptions.Timeout:
        cat_fact = "The request to fetch cat fact timed out."
        status = "error"
    except Exception as e:
        cat_fact = str(e)
        status = "error"

    data = {
        "status": status,
        "user": profile,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "fact": cat_fact,
                    
    }

    return JsonResponse(data,  status=200 if status == "success" else 502)