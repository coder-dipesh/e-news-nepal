from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from accounts.forms import ProfileForm

from editors.models import NewsModel


# def report_news(request):
#     form = ReportNewsForm(request.POST, request.FILES)
#     if request.method == "POST":
#         if form.is_valid():
#             title = request.POST['title']
#             name = request.POST['name']
#             email = request.POST['email']
#             contact = request.POST['contact']
#             category = request.POST['category']
#             content = request.POST['content']
#             image = request.FILES['image']

#             NewsModel.objects.create(
#                 name=name, email=email, contact=contact, title=title, category_id=category, content=content,
#                 image=image)

#         messages.success(request, "News Reported Successfully!!")
#         return redirect('/users/report_news')

#     context = {'form': ReportNewsForm,
#                'activate_report_news': 'active'}
#     return render(request, 'users/reportnews.html', context)


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


def about_us(request):
    return render(request, 'users/aboutus.html')

def contact_us(request):
    return render(request, 'users/contactus.html')


    #This is the account page for the user.
def account(request):
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
            return redirect('profile.html')
        else:
            messages.add_message(request, messages.ERROR,
                                 "Something went wrong!")
            context = {'profileForm': userdata}
            return render(request, 'users/profile.html', context)
    context = {'profileForm': userdata,
               'activate_profile': 'active'}
    return render(request, 'users/profile.html')