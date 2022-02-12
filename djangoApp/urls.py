from django.urls import path
from . import views

urlpatterns = [
    path('', views.myFunction, name='index'),
    path('about', views.myFunctionAbout, name='about'),
    path('add/<int:a>/<int:b>', views.add, name='add'),
    path('intro/<str:name>/<int:age>', views.intro, name='intro'),
    path('myfirstpage', views.myFristPage, name='myfirstpage'),
    path('mysecondpage', views.mySecondPage, name='mysecondpage'),
    path('mythirdpage', views.myThirdPage, name='mythirdpage'),
    path('myimagepage', views.myImagePage, name='myimagepage'),
    path('myimagepage2', views.myImagePage2, name='myimagepage2'),
    path('myimagepage3', views.myImagePage3, name='myimagepage3'),
    path('myimagepage4', views.myImagePage4, name='myimagepage4'),
    path('myimagepage5/<str:imagename>', views.myImagePage5, name='myimagepage5'),
]