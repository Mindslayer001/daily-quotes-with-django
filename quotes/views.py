from django.shortcuts import render
import requests
# Create your views here.
def getRandomQuotation(request):
    url = f"https://api.quotable.io/quotes/random"
    response = requests.get(url)
    data = response.json()
    context = {
        "author" : data[0]['author'],
        "content" : data[0]['content']
    }
    return render(request, "quotes/index.html", context)