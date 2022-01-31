from .models import FeedBack
from django.forms import ModelForm, Textarea

class FeedBackForm(ModelForm):
    class Meta:
        model = FeedBack
        fields = ['data']
        widgets = {"data": Textarea(attrs={
            'placeholder': 'Еnter a review'
        })}