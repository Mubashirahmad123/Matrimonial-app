from django.urls import path
from . import views


app_name = 'app'

urlpatterns = [
    path('new_profile/', views.NewProfileView, name='new_profile'), #CREATE
    path('', views.ProfileListView, name = 'profile_list'), #READ
    path('<int:profile_id>/profile_detail/', views.ProfileDetailView, name='profile_detail'), #READ
    path('<int:profile_id>/update', views.ProfileUpdateView, name='profile_update'), #UPDATE
    path('<int:profile_id>/delete', views.ProfileDeleteView, name='profile_delete'), #DELETE


    path('Contact', views.ContactView, name='contact'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('delete/', views.delete_view, name='delete'),
    # path('verify_email/<str:token>', views.verify_email_view, name='verify_email'),

    # path('compose_message/', views.ComposeMessageView, name='compose_message'),
    path('compose_message/<int:receiver_id>/', views.ComposeMessageView, name='compose_message'),

    path('send_message/<int:receiver_id>/', views.send_message, name='send_message'),
    path('message_history/<int:receiver_id>/', views.message_history, name='message_history'),
    path('message_inbox/', views.MessageRetrievalView, name='message_inbox'),

]


