from django.shortcuts import render,redirect
from .models import Sponsor
from .forms import SponsorForm
from .models import Subscribe
# Create your views here.

def create_sponsor(request):
    form = SponsorForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('create_sponsor')
    else:
        form = SponsorForm()
    return render(request,'sponsor/sponsor.html',{'form':form})
def create_subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        Subscribe.objects.create(email=email)
    return render(request,'subscribe.html')