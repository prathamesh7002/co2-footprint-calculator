from django import forms
from co2_footprint.models import CO2_footprint

class Co2_Form(forms.ModelForm):
    class Meta:
        model = CO2_footprint
        fields = ['name', 'electricity', 'travel', 'electronics_devices', 'food_habbit', 'water', 'waste']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'electricity': forms.NumberInput(attrs={'class': 'form-control'}),
            'travel': forms.NumberInput(attrs={'class': 'form-control'}),
            'electronics_devices': forms.NumberInput(attrs={'class': 'form-control'}),
            'food_habbit': forms.TextInput(attrs={'class': 'form-control'}),
            'water': forms.NumberInput(attrs={'class': 'form-control'}),
            'waste': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Name',
            'electricity': 'Electricity Consumption (kWh)',
            'travel': 'Travel Distance (km)',
            'electronics_devices': 'Electronics Devices Usage (hours)',
            'food_habbit': 'Food Habit',
            'water': 'Water Consumption (liters)',
            }
