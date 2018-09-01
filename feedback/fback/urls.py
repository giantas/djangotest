from django.conf.urls import url
from .views import FeedbackCreateView, success
from django.contrib.auth.decorators import login_required

app_name = 'feedback'

urlpatterns = [
    url(r'^form/$', login_required(FeedbackCreateView.as_view()), name='form'),
    url(r'^success/$',  login_required(success), name='success')
]