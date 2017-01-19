from django.shortcuts import render
from django.views.generic import View
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.conf import settings


class ContactView(View):
    """
    View that handles the contact form
    GET: Displays the contact form
    POST: If the data is OK, it sends and email and displays a correct message.
          If not, it displays the corresponding fields with errors
    """

    def get(self, request):
        return render(request, 'contact.html', {'contact_form': ContactForm()})

    def post(self, request):
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            sender = contact_form.cleaned_data['email']
            message = contact_form.cleaned_data['message']

            email_subject = 'New message from the Contact Form!'
            email_body = name + ' (email: ' + sender + ') send us this message: \n\n' + message

            mail = EmailMessage(email_subject,
                                email_body,
                                sender,
                                [settings.EMAIL_RECEIVER], headers={'Reply-To': sender})
            mail.send()
            return render(request, 'contact.html',
                          {'contact_form': contact_form,
                           'result_message': 'Message was sent! We will answer as soon as posible.'})
        else:
            return render(request, 'contact.html', {'contact_form': contact_form})