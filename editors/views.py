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
    allNews = NewsModel.objects.all()
    allNewsCount = allNews.count()
    myNewsCount = NewsModel.objects.filter(user_id=request.user.id).count()

    context = {
        'myNewsCount': myNewsCount,
        'allNewsCount': allNewsCount,
        'allNews': allNews,
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
    context = {'profileForm': userdata,
               'activate_profile': 'active'}

    return render(request, 'editors/editorsProfile.html', context)


@login_required
@editor_only
def addNews(request):
    user = request.user.id
    form = NewsForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            title = request.POST['title']
            category = request.POST['category']
            content = request.POST['content']
            image = request.FILES['image']

            NewsModel.objects.create(
                title=title, category_id=category, content=content, image=image, user_id=user)
            messages.add_message(request, messages.SUCCESS,
                                 'News added successfully!')
            return redirect('/editors/add-news')

    context = {'form': NewsForm,
               'activate_add_news': 'active'}
    return render(request, 'editors/news/newsForm.html', context)


@login_required
@editor_only
def updateNews(request, news_id):
    news = NewsModel.objects.get(id=news_id)
    if request.method == 'POST':
        newsForm = NewsForm(request.POST, request.FILES, instance=news)
        if newsForm.is_valid():
            newsForm.save()
            messages.add_message(request, messages.SUCCESS,
                                 'News updated successfully!')
            return redirect('/editors/update-news/' + str(news_id))
    context = {'form': NewsForm(instance=news),
               'activate_add_news': 'active',
               }
    return render(request, 'editors/news/newsUpdateForm.html', context)


@login_required
@editor_only
def deleteNews(request, news_id):
    news = NewsModel.objects.filter(id=news_id)
    news.delete()
    messages.add_message(request, messages.SUCCESS,
                         'News deleted successfully!')
    return redirect('/editors/my-news')


@login_required
@editor_only
def myNews(request):
    myNews = NewsModel.objects.filter(user_id=request.user.id)
    context = {'myNews': myNews,
               'activate_my_news': 'active'}
    return render(request, 'editors/news/newsView.html', context)
