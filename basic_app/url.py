from django.urls import path
from . import views
from django.conf.urls import url

app_name='basic_app'  ##this name is using in html template

urlpatterns = [
    path('',views.SchoolListView.as_view(),name='list'),  ##this name is using in html template
    path('create/',views.SchoolCreateView.as_view(),name='create'),
    path('add_student/',views.StudentCreateView.as_view(),name='add_student'),
    path('student_success/',views.StudentCreateSuccess.as_view(),name='student_form_success'),
    url(r'^update/(?P<pk>[-\w]+)/$',views.SchoolUpdateView.as_view(),name='update'),
    url(r'^delete/(?P<pk>[-\w]+)/$',views.SchoolDeleteView.as_view(),name='delete'),
    url(r'^(?P<pk>[-\w]+)/$',views.SchoolDetailsView.as_view(),name='details'),
]
