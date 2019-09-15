from django.urls import path
from django.conf.urls import url
from django.urls import path,include
import grievance.views as VIEWS
from django.conf.urls.static import static
from django.conf import settings


app_name = 'grievance'
urlpatterns =[
	# path('', VIEWS.HomeView.as_view())
	path('level1/', VIEWS.level1HomeView.as_view()),
	url(r'^level1/(?P<type>[a-z]+)$',VIEWS.level1RequestView.as_view()),
	path('', include('django.contrib.auth.urls')),
	path('level1/<student_id>', VIEWS.level1StudentView.as_view()),
	path('redirect/', VIEWS.RedirectView.as_view()),
	path('student/', VIEWS.studentHomeView.as_view()),
	path('psd/', VIEWS.updateLastSubmissionDate.as_view()),
	# path('temp/', VIEWS.TEMP.as_view()),

]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

