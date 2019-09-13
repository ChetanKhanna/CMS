from django.urls import path
from django.conf.urls import url
from django.urls import path,include
import grievance.tempViews as VIEWS

app_name = 'grievance'
urlpatterns =[
	path('', VIEWS.HomeView.as_view()),
	path('form/', VIEWS.FormView.as_view()),
	path('adduser/', VIEWS.AddView.as_view()),
	path('cmo/', VIEWS.CMO.as_view()),
	path('accounts/', include('django.contrib.auth.urls')),
]
