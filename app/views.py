from django.shortcuts import render,get_object_or_404,redirect
from .models import profile
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
from .models import Message
from .forms import MessageForm  # Create this form in your forms.py file
# from django import models
from django.urls import reverse
from django.contrib.auth.models import User  # Import the User model
from django.db import models  # Correct import
from django.db.models import Q
# from notifications.models import Notification







# Create your views here.

def ProfileListView(request):
    profiles = profile.objects.all()

    return render(request, 'app/profile_list.html',{'profiles':profiles})


@login_required
def ProfileDetailView(request, profile_id):
    # Use get_object_or_404 to retrieve the profile
    profile_obj = get_object_or_404(profile, id=profile_id)
    


    send_message_url = reverse('app:send_message', args=[profile_obj.id])


    # Retrieve notifications for the currently logged-in user
    # notifications = Notification.objects.filter(recipient=request.user)

    return render(request, 'app/profile_detail.html', {'profile_obj': profile_obj,'send_message_url':send_message_url})


@login_required
def ProfileDeleteView(request, profile_id):
    profile_to_delete = get_object_or_404(profile, id=profile_id)
    profile_to_delete.delete()
    profiles = profile.objects.all()
    return render(request, 'app/profile_list.html', {'profiles': profiles})


# def ProfileDeleteView(request, profile_id):
#     profile_to_delete = get_object_or_404(profile, id=profile_id)
#     profile_to_delete.delete()
#     profiles = profile.objects.all()
#     return render(request, 'app/profile_list.html', {'profiles': profiles})


# def ProfileDeleteView(request, profile_id):
#     if request.method == 'POST':
#         profile_to_delete = get_object_or_404(profile, id=profile_id)
#         profile_to_delete.delete()
#         messages.success(request, 'Profile deleted successfully.')
#         return redirect('app:profile_list')
#     else:
#         # Handle GET request (may not be necessary)
#         return redirect('app:profile_list')
    


# def ProfileDeleteView(request, profile_id):
#     if request.method == 'POST':
#         print("Hlo")
#         profile_to_delete = get_object_or_404(profile, id=profile_id)
#         print("hii")
#         profile_to_delete.delete()
#         print("HELlo")
#         messages.success(request, 'Profile deleted successfully.')
#         print("Thanks")
#         return redirect('app:profile_list')
#     else:
#         # Handle GET request (may not be necessary)
#         return redirect('app:profile_list')




# def ProfileDeleteView(request, profile_id):
#     if request.method == 'POST':
#         try:
#             profile_to_delete = get_object_or_404(profile, id=profile_id)
#             profile_to_delete.delete()
#             messages.success(request, 'Profile deleted successfully.')
#             return redirect('app:profile_list')
#         except Exception as e:
#             print(f"Error deleting profile: {e}")
#             # Add more detailed error handling here if needed
#     else:
#         # Handle GET request (may not be necessary)
#         return redirect('app:profile_list')






# def ProfileDeleteConfirmationView(request, profile_id):
#     print("Hlo")
#     profile_obj = get_object_or_404(profile, id=profile_id)
#     print("hii")
#     return render(request, 'app/profile_delete_confirmation.html', {'profile_obj': profile_obj})







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



def logout_view(request):
    logout (request)
    if request.method == "POST":
        return JsonResponse({'success': True})
    return redirect ('app:login')




def delete_view(request):
    request.user.delete()
    messages.success(request, 'Your account Has Been Deleted ')
    
    return redirect('app:login')





@login_required
def send_message(request, receiver_id):
    receiver = get_object_or_404(User, id=receiver_id)
    print("######")
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.sender = request.user
            new_message.receiver = receiver  # Set the receiver
            new_message.save()
            messages.success(request, 'Message sent successfully!')

            return redirect('view_profile', receiver_id)
    else:
        form = MessageForm()
    return render(request, 'app/compose_message.html', {'form': form})


# @login_required
# def MessageRetrievalView(request):
#     received_messages = Message.objects.filter(receiver=request.user).order_by('-timestamp')
#     return render(request, 'app/message_inbox.html', {'received_messages': received_messages})


# @login_required
# def MessageRetrievalView(request):
#     if request.user.is_authenticated:
#         print("User is authenticated:", request.user)
#     else:
#         print("User is not authenticated:", request.user)

#     received_messages = Message.objects.filter(receiver=request.user).order_by('-timestamp')
#     return render(request, 'app/message_inbox.html', {'received_messages': received_messages})



# @login_required
# def MessageRetrievalView(request):
#     if request.user.is_authenticated:
#         print("User is authenticated:", request.user)

#         received_messages = Message.objects.get(receiver=request.user).order_by('-timestamp')

#         return render(request, 'app/message_inbox.html', {'received_messages': received_messages})
#     else:
#         # Handle the case when the user is not authenticated, e.g., redirect to a login page.
#         # You can customize this part based on your application's requirements.
#         return HttpResponse("Please log in to access your messages.")


def MessageRetrievalView(request):
    if request.user.is_authenticated:
        print("User is authenticated:", request.user)
        print("User type:", type(request.user))  # Debug statement
        received_messages = Message.objects.filter(receiver=request.user ).order_by('-timestamp')
        return render(request, 'app/message_inbox.html', {'received_messages': received_messages})
    else:
        return HttpResponse("Please log in to access your messages.")








@login_required
def message_history(request, receiver_id):
    # Get message history between the logged-in user and the receiver
    messages = Message.objects.filter(
        (models.Q(sender=request.user, receiver_id=receiver_id) |
         models.Q(sender_id=receiver_id, receiver=request.user))
    ).order_by('timestamp')

    return render(request, 'app/message_history.html', {'messages': messages})

@login_required
def ComposeMessageView(request, receiver_id ):
    if request.method == 'POST':
        print("hlo")

        form = MessageForm(request.POST)
        if form.is_valid():
            print("tyyu")
            new_message = form.save(commit=False)
            print("niii")
            new_message.sender = request.user
            print("work")
            new_message.receiver = get_object_or_404(User, id=receiver_id )  # Include the receiver
            print("worked")
            new_message.save()
            return redirect('message_history', receiver_id=receiver_id)  # Specify the correct view name to redirect to
    else:
        form = MessageForm()
    return render(request, 'app/compose_message.html', {'form': form})


# @login_required
# def SendMessageView(request, receiver_id):
#     receiver = get_object_or_404(User, id=receiver_id)

#     if request.method == 'POST':
#         form = MessageForm(request.POST)
#         if form.is_valid():
#             message = form.save(commit=False)
#             message.sender = request.user
#             message.receiver = receiver
#             message.save()
#             messages.success(request, 'Message sent successfully!')
#             return redirect(reverse('app:profile_detail', args=[receiver.profile.id]))

#     form = MessageForm()
#     return render(request, 'app/compose_message.html', {'form': form, 'receiver': receiver})

# @login_required
# def MessageHistoryView(request, receiver_id):
#     receiver = get_object_or_404(User, id=receiver_id)
#     messages_received = Message.objects.filter(sender=receiver, receiver=request.user)
#     messages_sent = Message.objects.filter(sender=request.user, receiver=receiver)
#     messages = (messages_received | messages_sent).order_by('timestamp')

#     return render(request, 'app/message_history.html', {'messages': messages, 'receiver': receiver})

