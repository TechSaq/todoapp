from django import forms
from bootstrap_datepicker_plus import DatePickerInput

class TodoForm(forms.Form):
    CATEGORY_CHOICES = (
        ('H', 'Home'),
        ('W', 'Work'),
        ('P', 'Play'),
        ('N', 'Normal')
    )
    description = forms.CharField(label='Description', 
                                max_length=100,
                                widget=forms.Textarea(attrs={
                                    'class': 'form-control description',
                                    'placeholder' : 'What do you need to do?'}))
    category = forms.ChoiceField(choices=CATEGORY_CHOICES,
                                widget=forms.Select(attrs={'class': 'form-control'}))
    due_date = forms.DateField(widget=DatePickerInput(attrs={'class': 'form-control'}, format='%d/%m/%Y'))
