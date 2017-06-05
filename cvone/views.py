from django.shortcuts import render
# from .models import Post


# Create your views here.
def cv(request):
    readycv = ''
    return render(request, 'cvone/cv.html', {'readycv': readycv})

