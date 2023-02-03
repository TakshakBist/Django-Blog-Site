from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from blog.models import Post
from .forms import UserRegistrationForm, UserUpdateForm, UpdateProfileForm


def register(request):
    if request.method != 'POST':
        form = UserRegistrationForm()
    else:  # checks if http request is post
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}. Login Now!')
            return redirect('login')

    context = {'form': form}
    return render(request, 'users/register.html', context)


@login_required
def profile(request):
    # import all post from blog.models Post table and filter according to current user
    post = Post.objects.all().filter(author=request.user)
    context = {
        'posts': post
    }
    return render(request, 'users/profile.html', context)


@login_required
def update_profile(request):

    if request.method != 'POST':
        u_form = UserUpdateForm(instance=request.user)
        p_form = UpdateProfileForm(instance=request.user.profile)
    else:
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = UpdateProfileForm(request.POST,
                                   request.FILES,  # profile picture update is expecting files
                                   instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            username = u_form.cleaned_data.get('username')
            messages.success(request, f'Account Updated for {username}')
            return redirect('profile')

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/update_profile.html', context)
