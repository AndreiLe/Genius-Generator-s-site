from .views import IndexView, ServiceView, PersonalView, BusinessView, TestView
from django.conf.urls import url

urlpatterns = (
    url(r'^$', IndexView.as_view(), name='main.index'),

    url(r'^service/$', ServiceView.as_view(), name='main.service'),

    url(r'^personal/$', PersonalView.as_view(), name='main.personal'),

    url(r'^business/$', BusinessView.as_view(), name='main.business'),

    url(r'^test/(?P<param1>[^\/]+)/$', TestView.as_view(), name='main.test'),
)
