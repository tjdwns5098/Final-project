from django.shortcuts import render

# Create your views here.
def myHomepage(request):
    return render(request, "myHomepage.html")