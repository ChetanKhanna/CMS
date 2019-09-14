from django.urls import path
from django.conf.urls import url
from django.urls import path,include
import grievance.views as VIEWS
from django.conf.urls.static import static
from django.conf import settings


app_name = 'grievance'
urlpatterns =[
	# path('', VIEWS.HomeView.as_view())
	path('cmo/', VIEWS.cmoHomeView.as_view()),
	url(r'^cmo/(?P<type>[a-z]+)$',VIEWS.cmoRequestView.as_view()),
	path('accounts/', include('django.contrib.auth.urls')),
	# path('temp/', VIEWS.TEMP.as_view()),

]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

