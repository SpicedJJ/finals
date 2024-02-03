# forms.py
from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'appointment_date']

    def clean_appointment_date(self):
        appointment_date = self.cleaned_data['appointment_date']

        if appointment_date <= timezone.now():
            raise ValidationError('Appointment date must be in the future.')

        return appointment_date
