# src/sales/forms.py
from django import forms

CHART__CHOICES = (
    #specify choices as a tuple
    #when user selects Bar chart it is stored as #1
    ("#1", "Bar chart"),
    ("#2", "Pie chart"),
    ("#3", "Line chart")
) 

class SalesSearchForm(forms.Form):
    book_title = forms.CharField(max_length=120)
    chart_type = forms.ChoiceField(choices=CHART__CHOICES)