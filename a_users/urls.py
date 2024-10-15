from django.urls import path
from . import views

urlpatterns = [
    path('profile',views.profile,name="profile"),
    path('profile-edit',views.profile_edit,name="profile-edit"),
    path('profile-onboarding',views.profile_edit,name="profile-onboarding"),
    path('settings',views.profile_settings,name="profile-settings"),
    path('emailchange',views.profile_emailchange,name='profile-emailchange'),
    path('emailverify',views.profile_emailverify,name='profile-emailverify'),

]