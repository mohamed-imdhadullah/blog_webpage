from django.shortcuts import render

# Create your views here.


#about view
def about(request):
    return render(request, 'about/about.html', {'title': 'About',})
