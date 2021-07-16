from django.contrib import admin
from django.urls import path,include
from app1 import views  

urlpatterns = [
    path('',views.HomepageView.as_view()),
    path('about/',views.AboutpageView.as_view()),
    path('weekly/',views.WeeklypageView.as_view()),
    path('services/',views.ServicespageView.as_view()),
    path('contact/',views.ContactpageView.as_view()),
    path('sign/',views.sign,name='sign'),
    path('users/',views.UserspageView.as_view()),
    path('feedback/',views.FeedbackpageView.as_view()),
]
