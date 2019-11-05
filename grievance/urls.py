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
	path('level1/type/<type>',VIEWS.level1RequestView.as_view()),
	path('level1/student/<student_id>', VIEWS.level1StudentView.as_view()),
	# path('level1/student-status/<student_id>', VIEWS.level1StudentStatusView.as_view()),
	path('level1/psd-student-status/student/<student_id>',VIEWS.ViewOnlyPSDStudentPageView.as_view()),
	path('', include('django.contrib.auth.urls')),
	path('redirect/', VIEWS.RedirectView.as_view()),
	path('student/', VIEWS.studentHomeView.as_view()),
	path('psd/', VIEWS.PSDHomeView.as_view()),
	path('level2/', VIEWS.level2HomeView.as_view()),
	path('level2/type/<type>', VIEWS.level2RequestView.as_view()),
	path('level2/student/<student_id>', VIEWS.level2StudentView.as_view()),
	path('<level>/student-status/student/<student_id>', VIEWS.ViewOnlyStudentPageView.as_view()),
	# path('temp/', VIEWS.TEMP.as_view()),
	path('website-admin/change-deadline', VIEWS.changeDeadlineView.as_view()),
	path('website-admin/add-user', VIEWS.addUser.as_view()),

]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

