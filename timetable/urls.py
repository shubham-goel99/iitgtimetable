from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name='timetable'
urlpatterns = [
	url(r'^$',views.timetables.as_view(),name='timetables'),
	url(r'^(?P<pk>[0-9]+)/$',views.result,name='result'),
]

urlpatterns=format_suffix_patterns(urlpatterns)
