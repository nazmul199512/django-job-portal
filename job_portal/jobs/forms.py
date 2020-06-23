from django import forms
from .models import *


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'first_name',
            'last_name',
            'Email',
            'subject',
            'message'
        ]


class JobListingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(JobListingForm, self).__init__(*args, **kwargs)
        self.fields['job_location'].widget.attrs['placeholder'] = 'Dhaka,Bangladesh'
        self.fields['Salary'].widget.attrs['placeholder'] = '60k-80k BDT, 4k-5k USD, Negotiable'
        self.fields['title'].widget.attrs['placeholder'] = 'Software Engineer, Web Designer'
        self.fields['application_deadline'].widget.attrs['placeholder'] = '2020-12-27'

    class Meta:
        model = JobListing
        exclude = ('user', 'image')
        labels = {
            "job_location": "Job Location",
            "published_on": "Publish Date"
        }


class JobApplyForm(forms.ModelForm):
    class Meta:
        model = ApplyJob
        fields = [
            'name', 'email'
        ]
