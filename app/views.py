from django.shortcuts import render,get_object_or_404,redirect
from .models import profile
from .forms import ContactForm, ProfileForm  # Use "ProfileForm" instead of "profileForm"
from django.forms import formset_factory
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required 
from .forms import RegistrationForm
from django.contrib import messages





# Create your views here.

def ProfileListView(request):
    profiles = profile.objects.all()
    return render(request, 'app/profile_list.html',{'profiles':profiles})



def ProfileDetailView(request, profile_id):
    # Use get_object_or_404 to retrieve the profile
    profile_obj = get_object_or_404(profile, id=profile_id)
    return render(request, 'app/profile_detail.html', {'profile_obj': profile_obj})

def ProfileDeleteView(request, profile_id):
    profile_to_delete = get_object_or_404(profile, id=profile_id)
    profile_to_delete.delete()
    profiles = profile.objects.all()
    return render(request, 'app/profile_list.html', {'profiles': profiles})

def ContactView(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

    
           print(f"Name: {form.cleaned_data['name']}")
           print(f"Email: {form.cleaned_data['email']}")
           print(f"Subject: {form.cleaned_data['subject']}")


    else:
        form = ProfileForm()   
    
    return render(request, 'app/contact.html', {'form': form})





# def NewProfileView(request):

#     if request.method == 'POST':

#         form = ProfileForm(request.POST, request.FILES)

#         if form.is_valid():

#             form.save()




#             return redirect('app:profile_list')



#     else:
#         form = ProfileForm()
 
#     return render(request, 'app/new_profile.html', {'form': form})


@login_required
def NewProfileView(request):

    if request.method == 'POST':
        print("Hlo")
        form = ProfileForm(request.POST, request.FILES)
        print("Hii")

        if form.is_valid():
            print("Worked")

            form.save()


            return redirect('app:profile_list')
        
    else:
        form = ProfileForm()

    return render(request, 'app/new_profile.html', {'form':form})







def register(request):
    if request.method =='POST':
        form =  RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:login')
    else:
        form = RegistrationForm()

    return render(request, 'app/register.html', {'form':form})


        



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('app:profile_list')  
        

    else:
        form = AuthenticationForm()

    return render(request, 'app/login.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('app:login')




def delete_view(request):
    request.user.delete()
    messages.success(request, 'Your accoyunt Has Been Deleted ')
    
    return redirect('app:login')





