from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from views import AdminCourseView

urlpatterns = patterns(
    '',
    url(r'^course/(?P<slug>[-a-zA-Z0-9_]+)$/', AdminCourseView.as_view(), name='course_admin'),
    url(r'^courses/$', TemplateView.as_view(template_name="courses.html")),
    url(r'^courses/new/$', TemplateView.as_view(template_name="new_course.html")),
    url(r'^courses/lessons/new/$', TemplateView.as_view(template_name="new_lesson.html")),
    url(r'^users/$', TemplateView.as_view(template_name="users.html")),
)