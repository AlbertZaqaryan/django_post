from django.shortcuts import render
# Create your views here.

def calc(request):
    return render(request, 'calculator.html')


def add(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    res = num1 + num2
    return render(request, 'result.html', {'res':res})

def sub(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    res = num1 - num2
    return render(request, 'result.html', {'res':res})

