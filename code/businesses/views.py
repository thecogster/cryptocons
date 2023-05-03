from django.shortcuts import render

# Create your views here.

def homepage(request):

    template = 'businesses/homepage.html'
    return render(request, template)