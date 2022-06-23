from django.core.paginator import Paginator
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from requests import post

from admins.models import Newsletter
from .models import UserOTP
import random
from django.core.mail import send_mail
from django.conf import settings
from editors.models import NewsModel
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.contrib import messages, auth
from accounts.auth import unauthenticated_user
from accounts.models import Profile
from users.forms import CommentForm
from users.forms import Comment

from django.core.mail import send_mail
from django.conf import settings
import uuid


@unauthenticated_user
def signIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if user.is_superuser and user.is_staff and user.is_active:
                print("working")
                return redirect('/admins')
            elif not user.is_superuser and user.is_staff and user.is_active:
                return redirect('/editors')
            elif not user.is_superuser and not user.is_staff and user.is_active:
                return redirect('/')
        else:
            print("working")
            messages.error(request, "Username or Password is Incorrect.")
            return render(request, 'accounts/signIn.html', {})
    context = {}
    return render(request, 'accounts/signIn.html', context)


def socialLogin(request):
    usr = request.user
    print(usr)
    Profile.objects.create(
        user=usr, username=usr.username, email=usr.email)


@unauthenticated_user
def signUp(request):
    if request.method == 'POST':
        get_otp = request.POST.get('otp')

        if get_otp:
            get_usr = request.POST.get('usr')
            usr = User.objects.get(username=get_usr)

            if int(get_otp) == UserOTP.objects.filter(user=usr).last().otp:
                usr.is_active = True
                usr.save()
                Profile.objects.create(
                    user=usr, username=usr.username, email=usr.email)
                messages.add_message(
                    request, messages.SUCCESS, f'"{usr.username}" verified and registered successfully!')
                return redirect('sign-in')
            else:
                messages.add_message(
                    request, messages.WARNING, 'Invalid OTP! Please check again. ')

                return render(request, 'accounts/signUp.html', {'otp': True, 'usr': usr})

        userdata = CreateUserForm(request.POST)
        username = request.POST.get('username')
        if userdata.is_valid():
            userdata.save()
            usr = User.objects.get(username=username)
            usr.is_active = False
            usr.save()

            usr_otp = random.randint(100000, 999999)
            db_otp = usr_otp
            UserOTP.objects.create(user=usr, otp=db_otp)
            mail_message = f"Hello {usr.username}, \nYour OTP is {usr_otp}.\n\nThank You!\nTeam e-News. "

            send_mail(
                "Welcome to e-News -  Verify Your Email",
                mail_message,
                settings.EMAIL_HOST_USER,
                [usr.email],
                fail_silently=False
            )
            return render(request, 'accounts/signUp.html', {'otp': True, 'usr': usr})
        else:
            messages.add_message(request, messages.ERROR,
                                 'Please enter a valid credentials!!')

    context = {'form': CreateUserForm}

    return render(request, 'accounts/signUp.html', context)


def signOut(request):
    request.session.clear()
    print("Logged Out Successfully!!")
    return redirect('/')


def home(request):
    news = Paginator(NewsModel.objects.filter(status='P'), 5)
    page = request.GET.get('page')
    news = news.get_page(page)
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            news_model = Newsletter()
            news_model.email = email
            news_model.save()
    context = {
        "news": news,
        'activate_home': 'current', }
    
    return render(request, 'accounts/home.html', context)


def viewnews(request, news_id):
    news = NewsModel.objects.get(id=news_id)
    commentForm = CommentForm(request.POST)
    comments = Comment.objects.filter(post=news).order_by('-id')
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            news_model = Newsletter()
            news_model.email = email
            news_model.save()

    if request.method == 'POST':
        commentForm = CommentForm(request.POST)
        if commentForm.is_valid():
            content = request.POST.get('content')
            comment = Comment.objects.create(
                post=news, user=request.user, content=content)
            comment.save()

    else:
        commentForm = CommentForm()

    is_liked = False
    if news.like.filter(id=request.user.id).exists():
        is_liked = True

    context = {"news": news,
               "form": commentForm,
               'comments': comments,
               'is_liked': is_liked,
               'total_likes': news.total_likes(),

               }
    return render(request, 'accounts/viewnews.html', context)


def deleteComment(request, id):
    comment = Comment.objects.get(id=id, user_id=request.user.id)
    comment.delete()
    return redirect('/viewnews/' + str(comment.post.id))


@login_required
def like_news(request):
    post = NewsModel.objects.get(id=request.POST.get('news_id'))
    is_liked = False
    if post.like.filter(id=request.user.id).exists():
        post.like.remove(request.user)
        is_liked = False
    else:
        post.like.add(request.user)
        is_liked = True

    return redirect('/viewnews/' + str(post.id))


# Reset Password
# Imports for sendin HTML as mail


def send_forget_password_mail(email, token, username):
    html_content = render_to_string(
        'accounts/resetPassword/reset_password_mail.html',
        {'title': "Reset Password", 'token': token, 'username': username})
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(
        # Subject
        'Your forget password link',
        # content
        text_content,
        # Sender
        settings.EMAIL_HOST_USER,
        # Receiver
        [email],

    )
    email.attach_alternative(html_content, "text/html")
    email.send()
    return True


def enterUsername(request):
    if request.method == 'POST':
        username = request.POST.get('username')

        if not User.objects.filter(username=username).first():
            messages.add_message(
                request, messages.ERROR, f"No user found with '{username}'  username.")
            return redirect('/reset-password-enter-username')

        print(username)
        user_obj = User.objects.get(username=username)
        token = str(uuid.uuid4())

        profile_obj = Profile.objects.get(user=user_obj)
        profile_obj.forget_password_token = token
        profile_obj.save()
        print(user_obj.email)
        send_forget_password_mail(user_obj.email, token, username)
        messages.add_message(
            request, messages.SUCCESS, 'An email is sent to user with password changing link.')
        return redirect('/reset-password-enter-username')

    return render(request, 'accounts/resetPassword/resetPasswordEnterUsername.html')


def resetPassword(request, token):
    profile_obj = Profile.objects.filter(forget_password_token=token).first()
    context = {'user_id': profile_obj.user.id}

    if request.method == 'POST':
        new_password = request.POST.get('password-1')
        confirm_new_password = request.POST.get('password-2')
        user_id = request.POST.get('user_id')

        if user_id is None:
            messages.add_message(request, messages.ERROR,
                                 'No user found with that username.')
            return redirect(f'/new-password/{token}/')

        if new_password != confirm_new_password:
            return redirect(f'new-password/{token}/')
        else:
            print(user_id)
            user_obj = User.objects.get(id=user_id)
            print(user_obj)

            user_obj.set_password(new_password)
            user_obj.save()
            return redirect('/reset-password-success')

    return render(request, 'accounts/resetPassword/newPassword.html', context)


def resetPasswordSuccess(request):
    return render(request, 'accounts/resetPassword/resetPasswordDone.html', )


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        newssearch = NewsModel.objects.filter(title__icontains=searched)
        return render(request, 'accounts/home.html', {'searched': searched, 'newssearch': newssearch})
    else:
        return render(request, 'accounts/home.html')


