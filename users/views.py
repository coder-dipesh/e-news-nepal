from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from users.forms import ReportNewsForm
from users.models import ReportNewsModel


def report_news(request):
    con = {'success': False}
    # user = request.user.id
    # form = ReportNewsForm(request.POST, request.FILES)
    if request.method == "POST":
        print(request.POST)
        form = ReportNewsForm(request.POST, request.FILES)
        form.save()
        print("Item created")

        messages.success(request,"News Reported Successfully!!")
    context = {'form': ReportNewsForm,
               'activate_report_news': 'active'}


    return render(request, 'users/reportnews.html', context)
