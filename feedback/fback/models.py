import pycountry
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

RATINGS_CHOICES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)


class Feedback(models.Model):
    user = models.ForeignKey(User, null=True, blank=False, on_delete=models.SET_NULL)
    contact = models.CharField(max_length=25, blank=False)
    neighbourhood = models.ForeignKey('Neighbourhood', null=True, blank=False, on_delete=models.SET_NULL)
    ratings = models.IntegerField(choices=RATINGS_CHOICES)
    comments = models.TextField()

    def __str__(self):
        return '{} - {}'.format(self.user, self.contact)

    class Meta:
        default_related_name = 'feedback_feedback'


class Neighbourhood(models.Model):
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(choices=[(i.alpha_2, i.name) for i in pycountry.countries],
                               default='KE', max_length=10)

    def __str__(self):
        return '{} - {}'.format(self.name, self.country)

    class Meta:
        default_related_name = 'feedback_neighbourhood'
