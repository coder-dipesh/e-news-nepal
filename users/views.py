from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from users.forms import ReportNewsForm
from users.models import ReportNewsModel


def report_news(request):
    user = request.user.id
    form = ReportNewsForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            rname = request.POST['rname']
            remail = request.POST['remail']
            rcontact = request.POST['rcontact']
            rcategory = request.POST['rcategory']
            rcontent = request.POST['rcontent']
            rimage = request.FILES['rimage']

            ReportNewsModel.objects.create(
                rname=rname, rcategory_id=rcategory, remail=remail, rcontent=rcontent, rcontact=rcontact,
                rimage=rimage, ruser_id=user)
            messages.add_message(request, messages.SUCCESS,
                                 'News Reported Successfully!')
            return redirect('/users/report_news')

    context = {'form': ReportNewsForm,
               'activate_report_news': 'active'}
    return render(request, 'users/reportnews.html', context)
