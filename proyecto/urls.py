from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.views.generic import TemplateView
from app.views import EnlaceListView, EnlaceDetailView

from rest_framework import routers
from app.views import EnlaceViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'links', EnlaceViewSet)
router.register(r'user', UserViewSet)
urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'app.views.hora_actual', name='hora_actual'),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', 'app.views.home', name='home'),
    url(r'^add/$', 'app.views.add', name='add'),
    url(r'^nuevo_usuario/$', 'app.views.nuevo_usuario', name='nuevo_usuario'),
    url(r'^plus/(\d+)$', 'app.views.plus', name='plus'),
    url(r'^minus/(\d+)$', 'app.views.minus', name='minus'),
    url(r'^categoria/(\d+)$', 'app.views.categoria', name='categoria'),

    url(r'^about/$', TemplateView.as_view(template_name='index.html'),name='about'),
    url(r'^enlaces/$', EnlaceListView.as_view(),name='enlaces'),
    url(r'^enlaces/(?P<pk>[\d]+)$', EnlaceDetailView.as_view(),name='enlace'),

    # url(r'^proyecto/', include('proyecto.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
url(r'^admin/', include(admin.site.urls)),
)
