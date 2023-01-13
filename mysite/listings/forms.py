from django import forms
from .models import Listing


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'condition', 'product_type', 'sale_type', 'price', 'main_photo', 'photo_1',
                  'photo_2', 'city', 'state', 'zipcode', 'contact_email', 'list_date']
