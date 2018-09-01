from django.contrib import admin
from .models import Feedback, Neighbourhood

admin.site.register([Feedback, Neighbourhood])
