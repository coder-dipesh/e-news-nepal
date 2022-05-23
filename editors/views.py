from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth

# Create your views here.
from accounts.auth import editor_only
from accounts.forms import ProfileForm

from editors.forms import NewsForm
from editors.models import NewsModel


@login_required
@editor_only
def editorDashboard(request):
    users = User.objects.all()

    admin_count = users.filter(is_superuser=1).count()
    editor_count = users.filter(is_superuser=0, is_staff=1).count()
    user_count = users.filter(is_superuser=0, is_staff=0).count()

    user_info = users.exclude(is_superuser=1)

    context = {'users': users,
               'editor_count': editor_count,
               'user_count': user_count,
               'user_info': user_info,

               }
    return render(request, 'editors/editorsDashboard.html', context)


@login_required
@editor_only
def editorProfile(request):
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
            return redirect('/editors/profile')
        else:
            messages.add_message(request, messages.ERROR,
                                 "Something went wrong!")
            context = {'profileForm': userdata}
            return render(request, 'editors/editorsProfile.html', context)
    context = {'profileForm': userdata}

    return render(request, 'editors/editorsProfile.html', context)


@login_required
@editor_only
def addNews(request):
    form = NewsForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            NewsModel.objects.update(user_id=request.user.id)
            messages.add_message(request, messages.SUCCESS,
                                 'News added successfully!')
            return redirect('/editors/add-news')

    context = {'form': NewsForm}
    return render(request, 'editors/news/newsForm.html', context)


@login_required
@editor_only
def updateNews(request):
    return render(request, 'editors/news/newsUpdateForm.html')


@login_required
@editor_only
def viewNews(request):
    return render(request, 'editors/news/newsView.html')
