from django.db import models

class Service(models.Model):
    weight = models.CharField(max_length=100)
    price = models.FloatField()
    stripe_checkout_link = models.URLField()

    def __str__(self):
        return self.weight


from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15)
    message = forms.CharField(widget=forms.Textarea)
