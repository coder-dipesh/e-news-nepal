from pickle import NONE
from turtle import update
from unicodedata import category
from unittest import result
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from accounts.auth import admin_only
from django.contrib.auth.models import User

from accounts.auth import admin_only, unauthenticated_user
from .models import Category, CustomUser, Site
# Create your views here.
from accounts.forms import CreateUserForm
from .forms import CustomUserForm, CreateUserForm, CategoryForm, SiteSetting
from enews import settings

from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from accounts.models import Profile
from editors.models import NewsModel

from users.models import *

# from django.utils.encoding import force_bytes, force_text
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

# for pdf
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import os
from django.core.mail import EmailMultiAlternatives

# ==============================================
# ============= ADMIN DASHBOARD ================
# ==============================================


@login_required
@admin_only
def adminDashbaord(request):
    users = User.objects.all()

    admin_count = users.filter(is_superuser=1).count()
    editor_count = users.filter(is_superuser=0, is_staff=1).count()
    user_count = users.filter(is_superuser=0, is_staff=0).count()
    category_count = Category.objects.all().count()
    news_count = NewsModel.objects.all().count()
    user_info = users.exclude(is_superuser=1)

    context = {'users': users,
               'admin_count': admin_count,
               'editor_count': editor_count,
               'user_count': user_count,
               'user_info': user_info,
               'news_count': news_count,
               'category_count': category_count,
               }
    return render(request, 'admins/adminDashboard.html', context)


# ==========================================
# ============= USER VIEW ================
# ===========================================

@login_required
@admin_only
def getUsers(request):
    users = User.objects.all()
    user_info = users.filter(is_superuser=0, is_staff=0)
    context = {'user_info': user_info,
               'activate_users': 'active'}

    return render(request, 'admins/allUsers.html', context)

# ==========================================
# ============= Editor CRUD ================
# ===========================================


@login_required
@admin_only
def getEditor(request):
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

    context = {'activate_editors': 'active',
               'editor_info': editor_info,
               'editor': editor,
               }
    return render(request, 'admins/adminEditor/editorPage.html', context)


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    # , link_callback=fetch_resources)
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


@login_required
@admin_only
def editorSignUp(request):
    if request.method == 'POST':
        cform = CustomUserForm(request.POST)
        form = CreateUserForm(request.POST)
        role = request.POST.get('role')
        salary = request.POST.get('salary')

        if form.is_valid():
            user = form.save()
            user.save()
            # Getting user and altering its value
            usr = User.objects.get(username=user.username)
            username = request.POST['username']
            password1 = request.POST['password1']
            user_email = request.POST['email']
            joined_date = user.date_joined

            usr = User.objects.get(username=username)
            usr.is_staff = True
            usr.save()  # Save user

            print(usr.first_name)
            print(usr.last_name)

            if cform.is_valid():
                CustomUser.objects.create(user=user, role=role, salary=salary)
                Profile.objects.create(
                    user=usr, username=usr.username, email=usr.email, firstname=usr.first_name, lastname=usr.last_name)

                template = get_template('admins/adminEditor/mailEditor.html')
                data = {'username': username,
                        'password': password1,
                        'email': user_email,
                        'joined_date': joined_date, }

                html = template.render(data)
                result = BytesIO()
                # , link_callback=fetch_resources)
                pdf = pisa.pisaDocument(
                    BytesIO(html.encode("ISO-8859-1")), result)
                pdf = result.getvalue()
                filename = 'Login_' + data['username'] + '.pdf'

                mail_subject = 'New Editor - Login Details'

                context = {
                    'username': username
                }

                template = get_template('admins/adminEditor/mail.html')
                message = template.render(context)
                to_email = user_email

                email = EmailMultiAlternatives(
                    mail_subject, "Login", settings.EMAIL_HOST_USER, [to_email])

                email.attach_alternative(message, "text/html")
                email.attach(filename, pdf, 'application/pdf')
                email.send(fail_silently=False)

                messages.add_message(
                    request, messages.SUCCESS, 'Editor registered successfully!!')

            # Getting user and altering its value
            username = request.POST.get('username')
            usr = User.objects.get(username=username)
            usr.is_staff = True
            usr.save()  # Save user

        else:
            messages.add_message(request, messages.ERROR,
                                 'Unable to register editor!!')
    context = {'form': CreateUserForm,
               'cform': CustomUserForm, }
    return render(request, 'admins/adminEditor/registerEditor.html', context)


@login_required
@admin_only
def removeEditor(request, editor_id):
    editor = User.objects.get(id=editor_id)
    editor.delete()
    messages.add_message(request, messages.SUCCESS,
                         'Editor removed successfully')
    return redirect('/admins/all-editors')


@login_required
@admin_only
def updateEditor(request, editor_id):
    editor_form = User.objects.get(id=editor_id)
    ceditor = CustomUser.objects.get(user_id=editor_id)
    user = editor_form.username
    email = editor_form.email

    if request.method == "POST":
        ceditor_form = CustomUserForm(request.POST, instance=ceditor)
        if ceditor_form.is_valid():
            ceditor_form.save()
            messages.add_message(request, messages.SUCCESS,
                                 "Editor's Information Updated Successfully")

        else:
            messages.add_message(request, messages.ERROR,
                                 "Unable to Update Editor's Information")

    context = {
        'cform': CustomUserForm(instance=ceditor),
        'user': user,
        'email': email,
        'activate_editors': 'active',
    }

    return render(request, 'admins/adminEditor/updateEditor.html', context)

# ==========================================
# ==============CATEGORY CRUD================
# ===========================================


@login_required
@admin_only
def getCategory(request):
    category = Category.objects.all()
    return render(request, 'admins/Category/categoryPage.html', {"category": category})


@login_required
@admin_only
def newCategory(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        form.save()
        messages.add_message(request, messages.SUCCESS,
                             'Category Added Successfully')
    return render(request, 'admins/Category/newCategory.html')


@login_required
@admin_only
def delete_category(request, P_id):
    category = Category.objects.get(id=P_id)
    category.delete()
    messages.add_message(request, messages.SUCCESS,
                         'Category deleted successfully')
    return redirect("all-category")


@login_required
@admin_only
def categoryupdatebutton(request):
    return render(request, "admins/Category/updateCategory.html")


@login_required
@admin_only
def update_category(request, p_id):
    category = Category.objects.get(id=p_id)

    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Category Updated Successfully')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Unable to update Category')

    return render(request, 'admins/Category/updateCategory.html', {"form": CategoryForm(instance=category)})

# ==============================================
# ============= News DASHBOARD ================
# ==============================================


@login_required
@admin_only
def getNews(request):
    news = NewsModel.objects.all()
    return render(request, 'admins/Allnews/Allnews.html', {"news": news})


@login_required
@admin_only
def SiteSettingss(request):
    sitee = Site.objects.get(pk=1)
    if request.method == 'POST':
        sitee = SiteSetting(request.POST, request.FILES, instance=sitee)

        if sitee.is_valid():
            sitee.save()
            setee = Site.objects.get(pk=1)
            messages.add_message(request, messages.SUCCESS,
                                 'Category Updated Successfully')
            return render(request, 'admins/site/sitesetting.html', {"sitee": setee})
        else:
            messages.add_message(request, messages.ERROR,
                                 'Unable to update site settings')
    return render(request, 'admins/site/sitesetting.html', {"sitee": sitee})


def allContact(request):
    contact = contactinfo.objects.all()

    context = {'contact': contact}

    return render(request, 'admins/contactUs.html', context)
