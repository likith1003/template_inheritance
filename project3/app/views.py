from django.shortcuts import render

# Create your views here.
def home(request):
    d = {
        'name':"Steve",
        "age":28,
        "pay":1500
    }
    return render(request, 'home.html', d)

def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        return render(request, 'login.html')
    return render(request, 'register.html')