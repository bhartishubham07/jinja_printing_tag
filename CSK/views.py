from django.shortcuts import render

# Create your views here.

def jinja_print(request):
    D = {'name': 'SHUBHAM', 'age':21}
    return render(request, 'jinja_print.html', context=D)