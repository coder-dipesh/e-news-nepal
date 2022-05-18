from unittest import result
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.auth import admin_only
from django.contrib.auth.models import User

from accounts.auth import admin_only, unauthenticated_user
from .models import CustomUser
# Create your views here.
from accounts.forms import CreateUserForm
from .forms import CustomUserForm,CreateUserForm
from enews import settings

from django.template.loader import render_to_string
from django.core.mail import EmailMessage


# from django.utils.encoding import force_bytes, force_text
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

# for pdf
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import os
from django.core.mail import EmailMultiAlternatives

@login_required
@admin_only
def adminDashbaord(request):
    users = User.objects.all()
    
    admin_count = users.filter(is_superuser=1).count()
    editor_count = users.filter(is_superuser=0,is_staff=1).count()
    user_count = users.filter(is_superuser=0,is_staff=0).count()
    
    user_info= users.exclude(is_superuser=1)
    
    
    context = {'users': users,
                'admin_count': admin_count,
                'editor_count': editor_count,
                'user_count': user_count,
                'user_info': user_info,
                
                }
    return render(request, 'admins/adminDashboard.html',context)

@login_required
@admin_only
def getUsers(request):
    users = User.objects.all()
    user_info = users.filter(is_superuser=0,is_staff=0)
    context = {'user_info': user_info,
                'activate_users':'active'}
    
    return render(request, 'admins/allUsers.html',context)


@login_required
@admin_only
def getEditor(request):
    users = User.objects.all()
    editor_info = users.filter(is_superuser=0,is_staff=1)
    role=[]
    salary=[]
    
    
    for i in users:
        if not i.is_superuser and i.is_staff:
            print(i)
            editor = CustomUser.objects.get(user=i)
            role.append(editor.role)
            salary.append(editor.salary)
    editor = zip(editor_info, role,salary)        
    
    context = {'activate_editors':'active',
                'editor_info': editor_info,
                'editor': editor,
                 }
    return render(request, 'admins/adminEditor/editorPage.html',context)




# ==========================================
# ===========================================
# ===========================================







def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)#, link_callback=fetch_resources)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None







@login_required
def editorSignUp(request):
    if request.method == 'POST':
        cform = CustomUserForm(request.POST)
        form = CreateUserForm(request.POST)
        role = request.POST.get('role')
        salary = request.POST.get('salary')
        
        if form.is_valid():
            user= form.save()
            user.save()
            # Getting user and altering its value 
            usr = User.objects.get(username = user.username)
            username = request.POST['username']
            password1 = request.POST['password1']
            user_email= request.POST['email']
            joined_date = user.date_joined

            usr = User.objects.get(username = username)
            usr.is_staff = True
            usr.save() # Save user
            if cform.is_valid():
                CustomUser.objects.create(user=user,role=role,salary=salary)
                
                template = get_template('admins/adminEditor/mailEditor.html')
                data = {'username': username,
                        'password': password1,
                        'email': user_email,
                        'joined_date':joined_date,} 
                
                html = template.render(data)
                result = BytesIO()
                pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)#, link_callback=fetch_resources)
                pdf = result.getvalue()
                filename = 'Login_' + data['username'] + '.pdf'
                
                
                mail_subject = 'New Editor - Login Details'

                context={
                    'username': username
                }
                
                template = get_template('admins/adminEditor/mail.html')
                message = template.render(context)
                to_email = user_email
                
                
                email = EmailMultiAlternatives(mail_subject, "Login", settings.EMAIL_HOST_USER ,[to_email])
                
                email.attach_alternative(message, "text/html")
                email.attach(filename, pdf, 'application/pdf')
                email.send(fail_silently=False)
                
            # Sending mail to editor with login credentials 
            
                #return HttpResponse(pdf, content_type='application/pdf')

                # force download
                # if pdf:
                #     response = HttpResponse(pdf, content_type='application/pdf')
                #     filename = "Login_%s.pdf" %(data['username'])
                #     content = "inline; filename='%s'" %(filename)
                #     #download = request.GET.get("download")
                #     #if download:
                #     content = "attachment; filename=%s" %(filename)
                #     response['Content-Disposition'] = content
                #     return response
            

            
                messages.add_message(request, messages.SUCCESS, 'Editor registered successfully!!')
        
        else:
            messages.add_message(request, messages.ERROR, 'Unable to register editor!!')
        
    context = {'form': CreateUserForm,
                'cform':CustomUserForm,}

    return render(request, 'admins/adminEditor/registerEditor.html', context)
