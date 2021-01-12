from django.urls import path
from question import views

urlpatterns=[
path('',views.home),
path('question1',views.Question1View.as_view()),
path('question2',views.Question2View),
path('question3',views.Question3View.as_view()),
]
