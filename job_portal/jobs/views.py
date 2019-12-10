from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .forms import *
from .models import *
from django.template.loader import get_template
from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.views.generic import ListView


def home(request):
    qs = JobListing.objects.all()
    jobs = JobListing.objects.all().count()
    user = User.objects.all().count()
    company_name = JobListing.objects.filter(company_name__startswith='P').count()
    paginator = Paginator(qs, 5)  # Show 4 jobs per page
    page = request.GET.get('page')
    try:
        qs = paginator.page(page)
    except PageNotAnInteger:
        qs = paginator.page(1)
    except EmptyPage:
        qs = paginator.page(paginator.num_pages)

    context = {
        'query': qs,
        'job_qs': jobs,
        'company_name': company_name,
        'candidates': user
    }
    return render(request, "home.html", context)


def about_us(request):
    return render(request, "jobs/about_us.html", {})



def service(request):
    return render(request, "jobs/services.html", {})


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return redirect('/')
    context = {
        'form': form
    }
    return render(request, "jobs/contact.html", context)


@login_required
def job_listing(request):

    query = JobListing.objects.all().count()

    qs = JobListing.objects.all().order_by('-published_on')
    paginator = Paginator(qs, 3) #Show 3 jobs per page
    page = request.GET.get('page')
    try:
        qs = paginator.page(page)
    except PageNotAnInteger:
        qs = paginator.page(1)
    except EmptyPage:
        qs = paginator.page(paginator.num_pages)

    context = {
        'query': qs,
        'job_qs':query

    }
    return render(request, "jobs/job_listing.html", context)


@login_required
def job_post(request):

    form = JobListingForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return redirect('/jobs/job-listing/')
    context = {
        'form': form,

    }
    return render(request, "jobs/job_post.html", context)



def job_single(request, id):
    job_query =  get_object_or_404(JobListing, id=id)

    context = {
        'q': job_query,
    }
    return render(request, "jobs/job_single.html", context)

def apply_job(request):
    if request.method == "POST":
        form = JobApplyForm(request.POST )

        if form.is_valid():
            user = form.save(commit=False)
            user_name = form.cleaned_data.get('name')
            user_email = form.cleaned_data.get('email')
            user.save()

            subject = "Contact form Received"
            message = user_name , "Your application received.Please send CV via this Email"
            email = EmailMessage(subject, message, [user_email])
            email.send()
            return redirect('/')
    else:
        form = JobApplyForm()


    return render(request, "jobs/job_apply.html", {'form': form})



class SearchView(ListView):
    model = JobListing
    template_name = 'jobs/search.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        return self.model.objects.filter(title__contains=self.request.GET['title'],
                                         job_location__contains=self.request.GET['job_location'],
                                         employment_status__contains=self.request.GET['employment_status'])


