from django.shortcuts import render,get_object_or_404,redirect
from .models import profile
from .forms import ContactForm, ProfileForm  # Use "ProfileForm" instead of "profileForm"
from django.forms import formset_factory






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
#         form = ProfileForm(request.POST)
#         if form.is_valid():
#             # Save the form data and create a new profile
#             profile_obj = form.save()
#             # Optionally, you can redirect to a success page or do something else here.
#     else:
#         form = ProfileForm()
 
#     return render(request, 'app/new_profile.html', {'form': form})



def NewProfileView(request):

    profile_formset= formset_factory(ProfileForm, extra=1)

    if request.method == 'POST':
        formset = profile_formset(request.POST, request.FILES)
        
        if formset.is_valid():
            for form in formset:
                if form.has_changed():
                    form.save()

            return redirect ('app:profile_list')
    else:
        formset = profile_formset()
        print('test---', formset)


    context = {
        'formset': formset,
    }
        

    
    return render (request, 'app/new_profile.html', context )




    


