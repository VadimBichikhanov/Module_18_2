from django.shortcuts import render

def class_based(request):
    return render(request, "class_based.html")

def function_based(request):
    return render(request, "func_based.html")