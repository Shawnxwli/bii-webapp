from django.conf.urls import patterns, url
from views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', browse,name='browse.browse'),
                       url(r'^page/(\d+)$', getPage,name='browse.getPage'),

                       url(r'^investigation/([^//]+)/$',investigation,name='browse.investigation'),
                       url(r'^investigation/([^//]+)/study/([^//]+)/$',study,name='browse.investigation.study'),
                       url(r'^investigation/([^//]+)/study/([^//]+)/assay/(\d+)$',assay,name='browse.investigation.study.assay'),
                       url(r'^investigation/([^//]+)/study/([^//]+)/sample/(\d+)$',sample,name='browse.investigation.study.sample'),

                       url(r'^study/([^//]+)/$',study,name='browse.study'),
                       url(r'^study/([^//]+)/assay/(-?\d)/$',assay,name='browse.study.assay'),
                       url(r'^study/([^//]+)/sample/(-?\d)/$',sample,name='browse.study.sample'),
                       #   url(r'^upload/',upload,name='upload'),
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       # url('^accounts/profile/', 'main.views.private_profile'),
                       # url('^profile/(\w+)', 'main.views.public_profile'),
                       # url(r'^profiles/', include('profiles.urls')),

)

