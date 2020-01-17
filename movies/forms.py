from django import forms

from .models import Reviews


class ReviewForm(forms.ModelForm):
    '''Форма отзывов'''

    class Meta:
        model = Reviews
        fields = ('name', 'email', 'text')


class ModelForm(object):
    pass


class CharField(object):
    pass