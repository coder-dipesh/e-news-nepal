from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth import update_session_auth_hash

# Create your views here.
from django.template.loader import get_template
from xhtml2pdf import pisa

from accounts.auth import editor_only
from accounts.forms import ProfileForm
from admins.models import CustomUser

from editors.forms import NewsForm, RequestNewsUpdateForm
from editors.models import NewsModel
from io import BytesIO

@login_required
@editor_only
def editorDashboard(request):
    allNews = NewsModel.objects.filter(status='P')
    requestedNewsCount = NewsModel.objects.filter(status='D').count()

    allNewsCount = allNews.count()
    myNewsCount = NewsModel.objects.filter(user_id=request.user.id).count()

    context = {
        'myNewsCount': myNewsCount,
        'allNewsCount': allNewsCount,
        'allNews': allNews,
        'requestedNewsCount': requestedNewsCount,
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
                title=title, category_id=category, content=content, image=image, user_id=user, status="Published")

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
def downloadEditorData(request):
    users = User.objects.all()
    editor_info = users.filter(is_superuser=0, is_staff=1)
    role = []
    salary = []
    for i in users:
        if not i.is_superuser and i.is_staff:
            print(i)
            editor = CustomUser.objects.get(user=i)
            role.append(editor.role)
            salary.append(editor.salary)
    editor = zip(editor_info, role, salary)

    template = get_template('editors/download/editorData.html')
    context = {'editor': editor}

    html = template.render(context)
    result = BytesIO()
    pdf = pisa.pisaDocument(
        BytesIO(html.encode("ISO-8859-1")), result)
    pdf = result.getvalue()

    return HttpResponse(pdf, content_type='application/pdf')


@login_required
@editor_only
def downloadAllNewsData(request):
    news = NewsModel.objects.all()
    news_info = news.filter(status="P")

    template = get_template('editors/download/allNewsData.html')
    context = {'news': news_info}

    html = template.render(context)
    result = BytesIO()
    pdf = pisa.pisaDocument(
        BytesIO(html.encode("cp1252")), result)
    pdf = result.getvalue()

    return HttpResponse(pdf, content_type='application/pdf')
@login_required
@editor_only
def myNews(request):
    myNews = NewsModel.objects.filter(user_id=request.user.id)
    context = {'myNews': myNews,
               'activate_my_news': 'active'}
    return render(request, 'editors/news/newsView.html', context)


@login_required
@editor_only
def request_news(request):
    request_news = NewsModel.objects.filter(status='D')

    context = {'request_news': request_news,
               'activate_request_news': 'active'}
    return render(request, 'editors/news/requestnews.html', context)


@login_required
@editor_only
def delete_request_news(request, news_id):
    news = NewsModel.objects.get(id=news_id)
    news.delete()
    messages.add_message(request, messages.SUCCESS,
                         'News deleted successfully!')
    return redirect('/editors/request_news')


@login_required
@editor_only
def publish_request_news(request, news_id):
    news = NewsModel.objects.get(id=news_id)
    news.status = "P"
    news.save()
    messages.add_message(request, messages.SUCCESS,
                         'News Published successfully!')
    return redirect('/editors/request_news')


@login_required
@editor_only
def update_request_news(request, news_id):
    news = NewsModel.objects.get(id=news_id)
    if request.method == 'POST':
        newsForm = RequestNewsUpdateForm(
            request.POST, request.FILES, instance=news)
        if newsForm.is_valid():
            newsForm.save()
            news.status = "P"
            news.save()
            messages.add_message(request, messages.SUCCESS,
                                 'News updated and published successfully!')
            return redirect('/editors/request_news')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error in updating news! Please check each field below.')

    context = {'newsform': RequestNewsUpdateForm(instance=news),
               'activate_add_news': 'active',
               }

    return render(request, 'editors/news/requestNewsUpdateForm.html', context)


#  Change Password


@login_required
@editor_only
def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.add_message(request, messages.SUCCESS,
                                 "Password changed successfully")
            return redirect('/editors/change-password')
        else:
            messages.add_message(request, messages.ERROR,
                                 "Please check the fields")
            return render(request, 'editors/changePassword/changePassword.html', {'user_password_change_form': form})
    context = {
        'user_password_change_form': PasswordChangeForm(request.user),

    }
    return render(request, 'editors/changePassword/changePassword.html', context)
