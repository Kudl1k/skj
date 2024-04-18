from django.shortcuts import render

# Create your views here.

rooms = [
    {'id': 1, 'name' : 'Room 1'},
    {'id': 2, 'name' : 'Room 2'},
    {'id': 3, 'name' : 'Room 3'}
]


def home(request):
    context = {
        'rooms': rooms,
        'title': 'Home Page',
    }
    return render(request, 'base/home.html', context)

def login(request):
    return render(request, 'base/login.html')

def signup(request):
    return render(request, 'base/singup.html')