from django.urls import path
from . import views

urlpatterns = [
    path('profile',views.profile,name="profile"),
    path('profile-edit',views.profile_edit,name="profile-edit"),
    path('profile-onboarding',views.profile_edit,name="profile-onboarding"),
]