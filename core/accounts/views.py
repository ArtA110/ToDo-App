from django.shortcuts import render
from accounts.forms import UserForm
from django.http import HttpResponseRedirect
# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            print('FORM VALID')
            return HttpResponseRedirect('/')
    user_form = UserForm()
    return render(request,'accounts/signup.html',context={'user_form':user_form})