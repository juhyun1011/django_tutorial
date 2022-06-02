import random
from django.shortcuts import render

# Create your views here.

#request는 반드시 함수의 첫번째 인자로 받아줘야 함. 마찬가지로 request는 항상 render의 첫번째 인자로.
def index(request):
    return render(request, 'index.html')

def dinner(request, name):
    menus = [{"name":"족발", "price":30000}, {"name":"햄버거", "price":5000}, {"name":"치킨", "price":20000}, {"name":"초밥", "price":15000}]
    pick = random.choice(menus)
    context = {
        'pick' : pick,
        'name' : name,
        'menus' : menus
    }
    
    return render(request, 'dinner.html', context)