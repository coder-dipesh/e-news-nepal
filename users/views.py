from django.shortcuts import render


# Create your views here.
def report_news(request):
    return render(request, 'users/reportnews.html')
