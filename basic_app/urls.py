from django.conf.urls import url
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    url('list', views.SchoolListView.as_view(), name='list'),
    url('detail', views.SchoolDetailView.as_view(), name='detail'),
]
