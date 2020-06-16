from django.shortcuts import render


# Create your views here.

def home(request):
    import requests
    import json
    api_request = requests.get("http://newsapi.org/v2/top-headlines?country=in&apiKey=<YOUR_API_KEY>")
    api = json.loads(api_request.content)
    return render(request, 'home.html', {'api': api})
