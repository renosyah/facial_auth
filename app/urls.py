from django.conf.urls import url 
from app import views 

urlpatterns = [ 
    url(r'^api/student$', views.student_add),
    url(r'^api/student/(?P<id>[-\w]+)$', views.student),
    url(r'^api/student/(?P<id>[-\w]+)/image$', views.image_profile),
    url(r'^api/student/(?P<nim>[-\w]+)/image/validate$', views.validate_image_profile),
]
