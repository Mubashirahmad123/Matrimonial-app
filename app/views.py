from django.shortcuts import render,get_object_or_404,redirect
from .forms import ContactForm, ProfileForm  
from django.forms import formset_factory
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required 
from .forms import RegistrationForm
from django.contrib import messages
# import uuid
# from django.contrib.sites.shortcuts import get_current_site
# from .models import CustomUser
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Message, profile, User as myuser
from .forms import MessageForm  # Create this form in your forms.py file
# from django import models
from django.urls import reverse
from django.contrib.auth.models import User  # Import the User model
from django.db import models  # Correct import
from django.db.models import Q
# from notifications.models import Notification




# Create your views here.


#CREATE VIEW

def homeView(request):
    return render(request, 'app/home.html')




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




#READ VIEW

def ProfileListView(request):
    profiles = profile.objects.all()

    return render(request, 'app/profile_list.html',{'profiles':profiles})



@login_required
def ProfileDetailView(request, profile_id):
    # Use get_object_or_404 to retrieve the profile
    profile_obj = get_object_or_404(profile, id=profile_id)
    print(f"Profile Picture URL: {profile_obj.profile_pic.url}")

    


    send_message_url = reverse('app:send_message', args=[profile_obj.id])


    # Retrieve notifications for the currently logged-in user
    # notifications = Notification.objects.filter(recipient=request.user)

    return render(request, 'app/profile_detail.html', {'profile_obj': profile_obj,'send_message_url':send_message_url})

#UPDATE VIEW


@login_required
def ProfileUpdateView(request, profile_id):
    profile_obj = get_object_or_404(profile, id=profile_id)  # Use profile_obj

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile_obj)

        if form.is_valid():
            form.instance = profile_obj  # Associate the form with the profile_obj
            form.save()
            return redirect('app:profile_list')
    else:
        form = ProfileForm(instance=profile_obj)

    return render(request, 'app/new_profile.html', {'form': form})







#DELETE VIEW

@login_required
def ProfileDeleteView(request, profile_id):
    profile_to_delete = get_object_or_404(profile, id=profile_id)
    profile_to_delete.delete()
    profiles = profile.objects.all()
    return render(request, 'app/profile_list.html', {'profiles': profiles})




#PROFILE DELETE CONFORMATION

# def ProfileDeleteConfirmationView(request, profile_id):
#     print("Hlo")
#     profile_obj = get_object_or_404(profile, id=profile_id)
#     print("hii")
#     return render(request, 'app/profile_delete_confirmation.html', {'profile_obj': profile_obj})



#CONTACT VIEW

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




#REGISTER VIEW

def register(request):
    if request.method =='POST':
        form =  RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # user = form.save(commit=False)
            # user.is_email_verified = False
            # user.email_verification_token = str(uuid.uuid4())
            # user.save()

            # current_site = get_current_site(request)
            # mail_subject = 'Activate your account'
            # activation_link = f"http://{current_site}/app/verify_email/{ user.email_verification_token }/"
            # message =f"Click the link to activate your account: { activation_link}"
            # send_mail( mail_subject,message, 'magicfix@gmail.com', [user.email])


            return redirect('app:login')
    else:
        form = RegistrationForm()

    return render(request, 'app/register.html', {'form':form})


# def verify_email_view(request, token):
#     try:
       
#        user = CustomUser.objects.get(email_verification_token=token)
#        if user:
#            user.is_email_verified = True
#            user.email_verification_token = None
#            user.save()
           
#            return redirect('app:login')
           
#     except:
#         return HttpResponse('Activation link is invalid  ')
    


#LOGIN VIEW

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            # if user.is_email_verified:
            login(request, user)
            return redirect('app:profile_list')  
        
            # else:
                # messages.error(request, "Please verify  your email")
                # return redirect ('App:login')

    else:
        form = AuthenticationForm()

    return render(request, 'app/login.html', {'form': form})



#LOGOUT VIEW

def logout_view(request):
    logout (request)
    if request.method == "POST":
        return JsonResponse({'success': True})
    return redirect ('app:login')



# ACCOUNT DELETE VIEW

def delete_view(request):
    request.user.delete()
    messages.success(request, 'Your account Has Been Deleted ')
    
    return redirect('app:login')




#SEND MESSAGE VIEW


@login_required
def send_message(request, receiver_id):
    receiver = get_object_or_404(User, id=receiver_id)
    current_profile = get_object_or_404(profile, id=receiver_id)

    print("######")
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            print("valid")
            new_message = form.save(commit=False)
            print("seen")
            new_message = Message(sender=current_profile, receiver_id=receiver_id, subject='Your subject', message='Your message')
            new_message.save()
            print("push")

            new_message.sender = request.user.profile
            print("meet")
            new_message.receiver = receiver  # Set the receiver
            new_message.save()
            print("SEND")
            messages.success(request, 'Message sent successfully!')

            return redirect('app:message_history', receiver_id=receiver_id)
    else:
        form = MessageForm()
    return render(request, 'app/compose_message.html', {'form': form})


# MESSAGE RETRIVAL

# @login_required
# def MessageRetrievalView(request):
#     received_messages = Message.objects.filter(receiver=request.user).order_by('-timestamp')
#     return render(request, 'app/message_inbox.html', {'received_messages': received_messages})




#RECEIVED MESSAGE VIEW

def MessageRetrievalView(request):
    print('--------In MessageRetrievalView-----')
    if request.user.is_authenticated:
        # print("User:", request.user)
        # print("User type:", type(request.user)) # Debug statement
        # user = User.objects.get(username='Thanos')
        # print(f'---{user=}')
        # user = request.user.id  # Get the user ID
        # print(f"UserID:{user}")
        received_messages = Message.objects.all().order_by('-timestamp')
        print("holly")

        # received_messages = Message.objects.filter(receiver=user).order_by('-timestamp')
        return render(request, 'app/message_inbox.html', {'received_messages': received_messages})
        print("finer")
    else:
        return HttpResponse("Please log in to access your messages.")






#MESSAGE HISTORY

@login_required
def message_history(request, receiver_id):

    # Get message history between the logged-in user and the receiver
    messages = Message.objects.filter(
        (models.Q(id=receiver_id) |
         models.Q(sender_id=receiver_id))
    ).order_by('timestamp')
    print("howdey")
    
    return render(request, 'app/message_history.html', {'messages': messages, 'receiver_id':receiver_id})

#COMPOSE MESSAGE

@login_required
def ComposeMessageView(request, receiver_id ):
    if request.method == 'POST':
        print("hlo")
        print(f'@@@@@@@@@@@@@@@@\n{profile.objects.all()}')
        form = MessageForm(request.POST)
        print(f'compose message--{form=}\n{request.FILES=}')
        print(f"{form=}")
        if form.is_valid():
            print("tyyu")
            new_message = form.save(commit=False)
            print("niii")
            print("receiver_id")
            # new_message.sender = profile.objects.get(id=request.user.id)
            new_message.sender=profile.objects.get(id=receiver_id)
            print("work")
            # receiver = User.objects.get(username='Thanos')
            # print(f'{receiver=}')
            # new_message.receiver = receiver 
            new_message.receiver = get_object_or_404(profile, id=receiver_id )  # Include the receiver
            print("worked")
            new_message.save()
            print("saved")
            return redirect('app:message_history', receiver_id=receiver_id)  
    else:
        form = MessageForm()
    return render(request, 'app/compose_message.html', {'form': form})


