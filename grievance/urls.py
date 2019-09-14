from django.urls import path
from django.conf.urls import url
from django.urls import path,include
import grievance.views as VIEWS

app_name = 'grievance'
urlpatterns =[
	# path('', VIEWS.HomeView.as_view())
	path('level1/', VIEWS.level1HomeView.as_view()),
	url(r'^level1/(?P<type>[a-z]+)$',VIEWS.level1RequestView.as_view()),
	path('accounts/', include('django.contrib.auth.urls')),
	path('level1/<student_id>', VIEWS.level1StudentView.as_view()),
	# path('temp/', VIEWS.TEMP.as_view()),

]
