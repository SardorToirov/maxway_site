from django.shortcuts import render

# Create your views here.

def home_max_way(request):
    return render(request, 'index.html')

def main_order(request):
    return render(request, 'order.html')
