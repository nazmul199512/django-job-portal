from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    Email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.first_name


JOB_TYPE = (
    ('Part Time', 'Part Time'),
    ('Full Time', 'Full Time'),
    ('Freelance', 'Freelancer'),
)

CATEGORY = (
    ('Web Design', 'Web Design'),
    ('Graphic Design', 'Graphic Design'),
    ('Web Developing', 'Web Developing'),
    ('Software Engineering', 'Software Engineering'),
    ('HR', 'HR'),
    ('Marketing', 'Marketing'),
)

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Any', 'Any'),
)


class JobListing(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             null=True, editable=False, blank=True)
    title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=200)
    employment_status = models.CharField(choices=JOB_TYPE, max_length=10)
    vacancy = models.CharField(max_length=10, null=True)
    gender = models.CharField(choices=GENDER, max_length=30, null=True)
    category = models.CharField(choices=CATEGORY, max_length=30)
    description = models.TextField()
    responsibilities = models.TextField()
    experience = models.CharField(max_length=100)
    job_location = models.CharField(max_length=120)
    Salary = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(blank=True, upload_to='media', null=True)
    application_deadline = models.DateTimeField()
    published_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("jobs:job-single", args=[self.id])


class ApplyJob(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name
