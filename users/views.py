from django.contrib import messages
from django.shortcuts import render, redirect
from users.forms import *
from editors.models import *
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from accounts.forms import ProfileForm
from accounts.auth import user_only
from admins.models import Newsletter


@user_only
def report_news(request):
    form = ReportNewsForm(request.POST, request.FILES)
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            news_model = Newsletter()
            news_model.email = email
            news_model.save()

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
               'activate_report_news': 'current', }

    return render(request, 'users/reportnews.html', context)


def about_us(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            news_model = Newsletter()
            news_model.email = email
            news_model.save()
    context = {
        'activate_about_us': 'current', }
    return render(request, 'users/aboutus.html', context)


def contact_us(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            news_model = Newsletter()
            news_model.email = email
            news_model.save()

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        message = request.POST['message']
        ins = contactinfo(name=name, email=email,
                          contact=contact, message=message)
        ins.save()
    context = {
        'activate_contact_us': 'current', }
    messages.success(request, "Message Successfully Sent!")
    return render(request, 'users/contactus.html', context)


@user_only
def account(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            news_model = Newsletter()
            news_model.email = email
            news_model.save()

    profile = request.user.profile  # Getting currently logged in user data
    user = User.objects.get(username=profile)
    print(user)
    userdata = ProfileForm(request.POST, request.FILES, instance=profile)

    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')

        print(profile)
        if userdata.is_valid():
            User.objects.filter(username=profile).update(
                first_name=firstname, last_name=lastname, email=email)
            userdata.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Profile data updated successfully!')
        else:
            messages.add_message(request, messages.ERROR,
                                 "Something went wrong!")
            context = {'profileForm': userdata}
            return render(request, 'users/profile.html', context)

    context = {'profileForm': userdata,
               'activate_profile': 'active'}

    return render(request, 'users/profile.html', context)
