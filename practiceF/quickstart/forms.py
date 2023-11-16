from .models import user_image
from django.forms import ModelForm

class user_image_form(ModelForm):

    class Meta:
        model = user_image
        fields = ['title','image_downloaded']
