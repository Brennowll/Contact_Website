from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Q
from contact.models import Contact
from contact.forms import ContactForm
# Create your views here.

def home(request):
    
    contacts = Contact.objects.order_by('-id') # pylint: disable=no-member
    
    context = {
        'css_name': ['css/style_home.css'],
        'contacts': contacts,
    }
    
    return render(request, 'index.html', context)

def edit(request, contact_id):
    
    single_contact = get_object_or_404(
        Contact,
        pk=contact_id
        )
    
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=single_contact)
        if form.is_valid():
            form.save()
            return redirect('contact:home')
    
    context = {
        'css_name': ['css/style_edit.css'],
        'title': 'Edit your contact',
        'edit': True,
        'contact': single_contact,
    }
    
    return render(request, 'edit.html', context)

def create(request):
    
    
    if request.method == 'POST':
        Contact.objects.create( # pylint: disable=no-member
            name=request.POST['name'],
            phone=request.POST['phone'],
            email=request.POST['email'],
            address=request.POST['address'],
        )
        
        return redirect('contact:home')
    
    context = {
        'css_name': ['css/style_edit.css'],
        'title': 'Create your contact',
        'edit': False,
    }
    
    return render(request, 'edit.html', context)

def search(request):
    
    search_value = request.GET.get('q', '').strip()
    
    if search_value == '':
        return redirect('contact:home')
    
    contacts = Contact.objects.filter( # pylint: disable=no-member
        Q(name__icontains=search_value) |
        Q(phone__icontains=search_value) |
        Q(email__icontains=search_value) |
        Q(address__icontains=search_value)
    ).order_by('-id')

    context = {
        'css_name': ['css/style_home.css'],
        'contacts': contacts,
    }
    
    return render(request, 'index.html', context)