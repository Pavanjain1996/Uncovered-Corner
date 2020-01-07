from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='Index'),
    path('Country/',views.country,name='Country'),
    path('Country/<int:pk>/',views.explore,name='Explore'),
    path('Search/',views.search,name='Search'),
    path('Feedback/',views.feedback,name='Feedback'),
    path('About/',views.about,name='About'),
    path('Thanks/',views.thanks,name='Thanks'),
    path('Administrator/',views.administrator,name='Administrator'),
    path('AdminLogin/',views.adminlogin,name='AdminLogin'),
    path('AdminLogout/',views.adminlogout,name='AdminLogout'),
    path('SendReply/<int:pk>/',views.sendreply,name='SendReply'),
    path('Solved/',views.solved,name='Solved'),
]
