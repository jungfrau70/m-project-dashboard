from django.shortcuts import render

# Create your views here.

def main(request): #메인 화면
    return render(
    request, 
    'index.html', 
    {})