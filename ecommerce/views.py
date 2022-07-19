from django.http import HttpResponse
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
# Create your views here.

def MainView(request):
    return render(request,'home/main.html')


def search(request):
    if request.method == 'POST':
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        }
        keyword = request.POST.get('keyword')
        
        try:
            page = requests.get(f'https://groceries.aldi.ie/en-GB/Search?keywords=milk',headers=headers).text
            soup = BeautifulSoup(page,'html.parser')
        except:
            pass

    
    return HttpResponse('Got it ')