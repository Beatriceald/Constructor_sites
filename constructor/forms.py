from django import forms
from . models import *

class AddDateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Раздел не выбран"
        self.fields['sub_category'].empty_label = "Подраздел не выбран"

    class Meta:
        model = Constructor
        fields = '__all__'