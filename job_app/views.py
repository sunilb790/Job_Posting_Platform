from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from job_app1.models import Job
from job_app2.models import Userprofile

# Create your views here.
def frontpage(request):
    jobs=Job.objects.order_by('-created_at')[0:3]
    return render(request, 'frontpage.html',{'jobs': jobs})

def register(request):
    if request.method == 'POST':
         form=UserCreationForm(request.POST)

         if form.is_valid():
            user = form.save()

            account_type=request.POST.get('account_type','job_seeker')

            if account_type=='employer':
                userprofile=Userprofile.objects.create(user=user,is_employer=True)
                userprofile.save()
            else:
                userprofile=Userprofile.objects.create(user=user)
                userprofile.save()



            login(request, user)
            return redirect('dashboard')
    else:
        form=UserCreationForm()
    return render(request, 'register.html',{'form':form})