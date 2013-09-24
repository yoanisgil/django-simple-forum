from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'forum.views.index', name='forum-index'),
    url(r'^(\d+)/$', 'forum.views.forum', name='forum-detail'),
    url(r'^topic/(\d+)/$', 'forum.views.topic', name='topic-detail'),
    url(r'^reply/(\d+)/$', 'forum.views.post_reply', name='reply'),
    url(r'newtopic/(\d+)/$', 'forum.views.new_topic', name='new-topic'),
)
