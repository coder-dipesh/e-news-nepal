from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from accounts.auth import editor_only

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
