from django.shortcuts import render

def index_home(request):
    return render (request,'website/index.html')
def index_about(request):
    return render (request,'website/about.html')
def index_contact(request):
    return render (request,'website/contact.html')
def index_elements(request):
    return render (request,'website/elements.html')

