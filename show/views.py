from django.shortcuts import render
from .models import RJProfile,Show
from blog.models import Blog
from django.utils import timezone
# Create your views here.

def rj_list(request):
    rj_list = RJProfile.objects.all()
    return render(request,'rj/rj_list.html',{'rj_list':rj_list})
def rj_details(request,id):
    rj = RJProfile.objects.get(id=id)
    rj_show = rj.host.all()
    return render(request,'rj/re_details.html',{'rj':rj,'rj_show':rj_show})

def show_details(request,id):
    show = Show.objects.get(id=id)
    return render(request,'show/show_details.html',{'show':show})

def show_schedule(request):
    previous_show = Show.objects.filter(date__lte=timezone.now())
    # upcoming_show = Show.objects.filter(date__gte=timezone.now())[0]
    upcoming_show = Show.objects.filter(date__gte=timezone.now()).first()


    su = Show.objects.filter(date__gte=timezone.now(), date__week_day=1)
    mo = Show.objects.filter(date__gte=timezone.now(), date__week_day=2)
    tu = Show.objects.filter(date__gte=timezone.now(), date__week_day=3)
    we = Show.objects.filter(date__gte=timezone.now(), date__week_day=4)
    th = Show.objects.filter(date__gte=timezone.now(), date__week_day=5)
    fr = Show.objects.filter(date__gte=timezone.now(), date__week_day=6)
    sa = Show.objects.filter(date__gte=timezone.now(), date__week_day=7)

    context = {
        'previous_show':previous_show,
        'upcoming_show':upcoming_show,
        'su': su,
        'mo': mo,
        'tu': tu,
        'we': we,
        'th': th,
        'fr': fr,
        'sa': sa,

    }
    return render(request,'show/show_schedule.html',context)

def home(request):
    previous_show = Show.objects.filter(date__lte=timezone.now())
    upcoming_show = Show.objects.filter(date__gte=timezone.now())[0]
    latest_music = Show.objects.all().order_by('-created')[0:3]
    rj = RJProfile.objects.filter()[:2]
    blog = Blog.objects.all()[0:3]
    su = Show.objects.filter(date__gte=timezone.now(), date__week_day=1)
    mo = Show.objects.filter(date__gte=timezone.now(), date__week_day=2)
    tu = Show.objects.filter(date__gte=timezone.now(), date__week_day=3)
    we = Show.objects.filter(date__gte=timezone.now(), date__week_day=4)
    th = Show.objects.filter(date__gte=timezone.now(), date__week_day=5)
    fr = Show.objects.filter(date__gte=timezone.now(), date__week_day=6)
    sa = Show.objects.filter(date__gte=timezone.now(), date__week_day=7)


    context = {
        'previous_show': previous_show,
        'upcoming_show': upcoming_show,
        'latest_music':latest_music,
        'rj': rj,
        'blog':blog,
        'su': su,
        'mo': mo,
        'tu': tu,
        'we': we,
        'th': th,
        'fr': fr,
        'sa': sa,

    }
    return render(request,'home.html',context)

