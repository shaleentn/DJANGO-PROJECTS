from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from .models import Resource, UserProfile
from .forms import SignUpForm, ResourceForm
from django.contrib.auth import login

class CustomLoginView(LoginView):
    template_name = 'login.html'

@login_required
def index(request):
    if request.user.is_authenticated:
        return redirect('resource_list')
    else:
        return render(request, 'index.html')
    
@login_required
def upload_resource(request):
    if request.user.userprofile.is_lecturer:  # Ensure only lecturers can upload
        if request.method == 'POST':
            form = ResourceForm(request.POST, request.FILES)
            if form.is_valid():
                resource = form.save(commit=False)
                resource.uploaded_by = request.user
                resource.department = request.user.userprofile.department  # Assign the department
                resource.save()
                return redirect('resource_list')
        else:
            form = ResourceForm()
        return render(request, 'upload_resource.html', {'form': form})
    else:
        return redirect('resource_list')
    
def index(request):
    if request.user.is_authenticated:
        return redirect('resource_list')
    return render(request, 'index.html')



@login_required
def resource_list(request):
    user_profile = UserProfile.objects.get(user=request.user)
    resources = Resource.objects.filter(department=user_profile.department)
    return render(request, 'DlsApp/resource_list.html', {'resources': resources})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user_profile = UserProfile.objects.create(user=user,
                                                       faculty=form.cleaned_data.get('faculty'),
                                                       department=form.cleaned_data.get('department'),
                                                       staff_id=form.cleaned_data.get('staff_id'))
            login(request, user)
            return redirect('resource_list')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})