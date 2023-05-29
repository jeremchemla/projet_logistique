from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
import stripe
from .models import Service, ContactForm

def index_view(request):
    return render(request, 'index.html')

def services_view(request):
    return render(request, 'services.html')

def about_view(request):
    return render(request, 'about.html')




stripe.api_key = settings.STRIPE_SECRET_KEY


def choose_service(request):
    services = Service.objects.all()  # ou toute autre queryset appropriée
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        service_id = request.POST.get('service')

        # Ici, vous pouvez enregistrer les informations de l'utilisateur dans votre base de données si vous le souhaitez

        service = Service.objects.get(pk=service_id)

        # send_mail(
        #         'Merci pour votre commande',
        #         f'Nous avons bien reçu votre commande {service} et nous la traiterons dans les plus brefs délais.',
        #         'm0534561463@gmail.com',  # Votre adresse e-mail
        #         [email],  # L'adresse e-mail du client
        #     )

            # Envoi de l'email de notification à vous-même
        send_mail(
             'Nouvelle commande en cours',
            f' quelqun a clique sur une commande {first_name} {last_name} ({email}, {phone}): {service}',
            'm0534561463@gmail.com',  # Votre adresse e-mail
            ['m0534561463@gmail.com'],  # Votre adresse e-mail
            )
        # Vous pouvez utiliser 'pricing' pour définir le prix dans votre lien de paiement Stripe Checkout

        return redirect(service.stripe_checkout_link)
    
    return render(request, 'index.html', {'services': services})  # Redirige l'utilisateur vers le lien de paiement Stripe Checkout


from django.shortcuts import render
from django.core.mail import send_mail

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            message = form.cleaned_data['message']

            # Envoi de l'email de confirmation au client
            send_mail(
                'Merci pour votre message',
                'Nous avons bien reçu votre message et nous y répondrons dans les plus brefs délais.',
                'm0534561463@gmail.com',  # Votre adresse e-mail
                [email],  # L'adresse e-mail du client
            )

            # Envoi de l'email de notification à vous-même
            send_mail(
                'Nouveau message de contact',
                f'Vous avez reçu un nouveau message de {name} ({email}, {phone_number}): {message}',
                'm0534561463@gmail.com',  # Votre adresse e-mail
                ['m0534561463@gmail.com'],  # Votre adresse e-mail
            )

            return HttpResponse('Merci pour votre message.')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

