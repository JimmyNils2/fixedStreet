from django.shortcuts import redirect, render, resolve_url
from .forms import ContactForm
from django.core.mail import EmailMessage
# Create your views here.

def contact(request):

    contact_form=ContactForm()

    if request.method=='POST':
        contact_form=ContactForm(data=request.POST)

        if contact_form.is_valid():
            
            name=request.POST.get('name')
            email=request.POST.get('email')
            content=request.POST.get('content')

            email=EmailMessage("Message from FixedStreet's App",f"The user with name: {name}\n with email: {email}\n says the following: {content}","",['jimmynils2@gmail.com'],reply_to=[email])

            try:
                email.send()
                return(redirect('/contact/?valido'))
            
            except:
                return(redirect('/contact/?novalido'))

    return(render(request,'contact/contact.html',{'contact_form':contact_form}))