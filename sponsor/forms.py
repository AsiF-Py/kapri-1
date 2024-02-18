from django import forms
from .models import Sponsor

class SponsorForm(forms.ModelForm):
    class Meta:
        model = Sponsor
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SponsorForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['placeholder'] = self.fields[field].label