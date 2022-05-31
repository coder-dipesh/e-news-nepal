from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from users.forms import ReportNewsForm
from users.models import ReportNewsModel
from editors.models import NewsModel


def report_news(request):
    form = ReportNewsForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            title = request.POST['title']
            name = request.POST['name']
            email = request.POST['email']
            contact = request.POST['contact']
            category = request.POST['category']
            content = request.POST['content']
            image = request.FILES['image']

            NewsModel.objects.create(
                name=name, email=email, contact=contact, title=title, category_id=category, content=content,
                image=image)

        messages.success(request, "News Reported Successfully!!")
        return redirect('/users/report_news')

    context = {'form': ReportNewsForm,
               'activate_report_news': 'active'}
    return render(request, 'users/reportnews.html', context)


def view_news(request):
    # form = ReportNewsForm(request.POST, request.FILES)
    # if request.method == "POST":
    # if form.is_valid():
    #     title = request.POST['title']
    #     name = request.POST['name']
    #     email = request.POST['email']
    #     contact = request.POST['contact']
    #     category = request.POST['category']
    #     content = request.POST['content']
    #     image = request.FILES['image']
    #
    #     NewsModel.objects.create(
    #         name=name, email=email, contact=contact, title=title, category_id=category, content=content, image=image)
    #     return redirect('/users/report_news')
    #
    # context = {'form': ReportNewsForm,
    #            'activate_report_news': 'active'}
    return render(request, 'users/viewnews.html')
