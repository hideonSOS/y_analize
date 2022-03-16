from django.urls import path, include
from . import views


urlpatterns=[
    path('', views.test),
    path('page1/', views.page1,name="page1"),
    path('page2/', views.page2,name="page2"),
    path('page3/', views.page3,name="page3"),
    path('page4/', views.page4,name='page4'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name = 'logout'),
    path('signup/', views.signup, name='signup'),
    
]