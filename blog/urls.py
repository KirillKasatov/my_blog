import functools
from django.conf.urls import include, url
from django.contrib.auth.views import logout


urlpatterns = [
    url(r'^$', 'blog.views.home', name='home'),
    url(r'^about/$', 'blog.views.about', name='about'),
    url(r'^article/(?P<article_id>[0-9]+)/$', 'blog.views.show_article', name='article'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', functools.partial(logout, next_page='home'), name='logout'),
    url(r'^registration/$', 'blog.views.regis', name='registration'),
    url(r'^addcomment/(?P<article_id>[0-9]+)/$', 'blog.views.show_article', name='comment'),

]
