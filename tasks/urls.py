from django.conf.urls import url
from .import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView



app_name = 'tasks'

urlpatterns = [

    # # /webpages/
    url(r'^$', views.IndexView.as_view(), name='index'),
    #
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    #
    url(r'^login_user/$', LoginView.as_view(template_name='tasks/login.html'), name='login_user'),
    url(r'^logout_user/$', LogoutView.as_view(template_name='webpages/login.html'), name='logout_user'),
    #
    # # webpages/<sample_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #
    # # /webpages/sample/add/
    url(r'sample/add/$', views.TaskCreate.as_view(), name='sample-add'),
    #
    # # /webpages/sample/2/
    url(r'sample/(?P<pk>[0-9]+)/$', views.TaskUpdate.as_view(), name='sample-update'),
    #
    # # /webpages/sample/2/delete/
    url(r'sample/(?P<pk>[0-9]+)/delete/$', views.TaskDelete.as_view(), name='sample-delete'),

]