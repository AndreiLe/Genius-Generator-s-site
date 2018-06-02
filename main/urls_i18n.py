from .views import IndexView, ProjectsView, MainView
from django.conf.urls import url

urlpatterns = (
    url(r'^$', IndexView.as_view(), name='main.index'),

    url(r'^projects/$', ProjectsView.as_view(), name='main.projects'),

    url(r'^main/$', MainView.as_view(), name='main.main'),
)
