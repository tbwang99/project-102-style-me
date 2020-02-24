from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import HomepageForm, EditProfileForm, MoreUserInfo

from django.views import generic
from .models import Homepage, UserProfile
from django.shortcuts import redirect

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.
class HomepageView(generic.CreateView):
    model = Homepage
    #form_class = HomepageForm
    template_name = 'users/homepage.html'
    fields = ['name', 'location', 'subject', 'courseNumber', 'time', 'description']
    #success_url = 'myapp/success.html'

# def register(request):
#     if request.method =='POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('users:home'))
#     else:
#         form = RegistrationForm()

#         args = {'form': form}
#         return render(request, 'users/reg_form.html', args)

def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'users/profile.html', args)

def edit_profile(request):
    try:
        user_instance = UserProfile.objects.get(user = request.user)
    except UserProfile.DoesNotExist:
        user_instance = UserProfile(user=request.user)
    if request.method == 'POST':
        user_form = EditProfileForm(request.POST, instance=user_instance)
        info_form = MoreUserInfo(request.POST, instance=user_instance)
        if user_form.is_valid() and info_form.is_valid():
            user_form.save()
            info_form.save()
            return redirect(reverse('users:view_profile'))
    else:
        user_form = EditProfileForm(instance=request.user)
        info_form = MoreUserInfo(instance=request.user)
        # args = {'form': form}
        return render(request, 'users/edit_profile.html', {'user_form': user_form,'info_form':info_form})



# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(data=request.POST, user=request.user)

#         if form.is_valid():
#             form.save()
#             update_session_auth_hash(request, form.user)
#             return redirect(reverse('users:view_profile'))
#         else:
#             return redirect(reverse('users:change_password'))
#     else:
#         form = PasswordChangeForm(user=request.user)

#         args = {'form': form}
#         return render(request, 'users/change_password.html', args)

class requestListView(generic.ListView):
    model = Homepage
    template_name = 'users/requestList.html'
