from django.shortcuts import render
from prs.forms import UserForm
from prs.models import User, ReportedCases

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    #num_books=Book.objects.all().count()
    #num_instances=BookInstance.objects.all().count()
    # Available books (status = 'a')
    #num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    #num_authors=Author.objects.count()  # The 'all()' is implied by default.
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        #context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
    )

def report(request):
    return render(
        request,
        'report.html',
    )

def areastatus(request):
    return render(
        request,
        'areastatus.html',
    )

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            email = request.POST.get('email', '')
            password = request.POST.get('password', '')
            user_obj = User(username=username, email=email, password=password)
            user_obj.save()
            return render(request, 'prs/register.html', {'user_obj': user_obj, 'is_registered':True})
        else:
            form = UserForm()
            return render(request, 'prs/register.html', {'form': form})
