from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')

            # TODO Enviar mail
            mail = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto",  # asunto
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),  # mensaje
                "no-contestar@inbox.mailtrap.io",  # quien envia el mensaje
                ["jose.d2.v@gmail.com"],  # quienes reciben el mensaje
                reply_to=[email],  # a quien responder
            )
            try:
                mail.send()
                return redirect(reverse('contact')+'?ok')
            except:
                return redirect(reverse('contact')+'?fail')

    return render(request, 'contact/contact.html', {'form': contact_form})