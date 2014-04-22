from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from movies import views

urlpatterns = patterns('',

    # Examples:
    url(r'^$', views.index, name='index'),


    #url(r'^login/', views.user_login, name="login"),
    #url(r'^logout/', views.user_logout, name="logout"),

    #url(r'^users/$', views.users, name="users"),
    #url(r'^users/(?P<user_id>\d+)', views.userdetail, name="userdetail"),

    #url(r'^movies/$', views.movies, name="movies"),

    #url(r'^test/$', views.test, name="test"),

	#new
	#url(r'^new$', views.new, name='new'),

	# ex: /polls/5/
	#url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),

	# ex: /polls/5/results/
	#url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),

	# ex: /polls/5/vote/
	#url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),

)