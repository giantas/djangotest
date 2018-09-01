import phonenumbers
from django.core.exceptions import ValidationError
from .models import Feedback, Neighbourhood, RATINGS_CHOICES
from django import forms


class FeedbackForm(forms.ModelForm):

    contact = forms.CharField(required=True, widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Phone Number'
        }))
    neighbourhood = forms.ModelChoiceField(widget=forms.Select(attrs={
            'class': 'form-control',
            'placeholder': 'Neighbourhood'
        }),
        queryset=Neighbourhood.objects.all())
    ratings = forms.ChoiceField(required=True, widget=forms.Select(attrs={
            'class': 'form-control',
            'placeholder': 'Ratings'
        }), choices=RATINGS_CHOICES)
    comments = forms.CharField(widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Comments'
        }))

    def clean(self):
        contact = self.cleaned_data['contact']
        region_name = self.cleaned_data['neighbourhood']
        hood = Neighbourhood.objects.get(name=region_name)
        try:
            res = phonenumbers.parse(contact, hood.country)
        except phonenumbers.phonenumberutil.NumberParseException:
            raise ValidationError('Invalid phone number')

        if not phonenumbers.is_valid_number(res):
            raise ValidationError('Invalid phone number')

        return self.cleaned_data

    class Meta:
        model = Feedback
        fields = ('contact', 'neighbourhood', 'ratings', 'comments')
