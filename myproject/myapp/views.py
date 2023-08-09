from django.shortcuts import render

# Create your views here.

dict={}

def create(request):
    if request.method == 'POST':
        key = request.POST.get('key')
        value = request.POST.get('value')
        dict[key] = value 
    return render(request , 'create.html')

def read(request):
    return render(request , 'read.html' , {'data':dict})

def update(request):
    if request.method == 'POST':
        key = request.POST.get('key')
        value = request.POST.get('value')
        if key in dict:
            dict[key] = value 
    return render(request , 'update.html')

def delete_view(request):
    if request.method == 'POST':
        key = request.POST.get('key')
        if key in dict:
            del dict[key]  # Remove the key from the dictionary
    return render(request, 'delete.html')