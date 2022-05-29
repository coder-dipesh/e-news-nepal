from django.contrib import messages
from django.shortcuts import render, redirect
from accounts.auth import unauthenticated_user

# Create your views here.
from users.forms import ReportNewsForm
from users.models import ReportNewsModel


@unauthenticated_user
def report_news(request):
    form = ReportNewsForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            contact = request.POST['contact']
            category = request.POST['category']
            content = request.POST['content']
            image = request.FILES['image']

            ReportNewsModel.objects.create(
                name=name, category_id=category, email=email, content=content, contact=contact,
                image=image)
        messages.success(request, "News Reported Successfully!!")
        return redirect('/users/report_news')

    context = {'form': ReportNewsForm,
               'activate_report_news': 'active'}
    return render(request, 'users/reportnews.html', context)
