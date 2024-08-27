from django.shortcuts import render,redirect
from . forms import ContactForm
from django.contrib import messages
from . models import Contact
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registered!')
            return redirect('index')
    conform = ContactForm()
    data = Contact.objects.all()
    return render(request, 'index.html', {'loginForm' : conform, 'data' : data})

def update(request,id):
    data = Contact.objects.get(id=id)
    if request.method == 'POST':
        data.name = request.POST.get('name')
        data.contact = request.POST.get('contact')
        data.email = request.POST.get('email')
        data.save()
        messages.success(request, 'Updated!')
        return redirect('index')

    
    return render(request, 'update.html', {'data' : data})

def delete(request,id):
    data = Contact.objects.get(id=id)
    data.delete()
    messages.success(request, 'Deleted!')
    return redirect('index')