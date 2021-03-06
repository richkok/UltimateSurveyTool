from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from survey import settings

admin.autodiscover()
media_url = settings.MEDIA_URL.lstrip('/').rstrip('/')

urlpatterns = patterns('',
                       url(r'^$', 'survey.views.index', name='home'),
                       url(r'^survey/(?P<p_id>\d+)/$', 'survey.views.survey_detail', name='survey_detail'),
                       url(r'^confirm/(?P<uuid>\w+)/$', 'survey.views.confirm', name='confirmation'),
                       url(r'^privacy/$', 'survey.views.privacy', name='privacy_statement'),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
                       )

# media url hackery. le sigh. 
urlpatterns += patterns('',
                        (r'^%s/(?P<path>.*)$' % media_url, 'django.views.static.serve',
                         {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
                        )
