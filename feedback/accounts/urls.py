from django.conf.urls import url
from .views import login_user, register_user, logout_user

app_name = 'accounts'

urlpatterns = [
    url(r'^login/$', login_user, name='login'),
    url(r'^logout/$', logout_user, name='logout'),
    url(r'^register/$', register_user, name='register'),
]