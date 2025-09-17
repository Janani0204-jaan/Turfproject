from django import forms
from .models import Booking, Turf

TURF_CHOICES = [
    ('The spark', 'the spark'),
    ('Nottam turf', 'Nottam turf'),
    ('Golozo turf', 'Golozo turf'),
    ('Lords turf', 'Lords turf'),
    ('Infinity areana cr7', 'Infinity areana cr7'),
    ('Y2 turf', 'Y2 turf'),
    ('Turfwar', 'Turfwar'),
    ('Turf 59', 'Turf 59'),
    ('Xtream turf', 'Xtream turf'),
    ('Spr turf', 'Spr turf'),
    ('Zam zam turf', 'Zam zam turf'),
    ('Champion zone turf', 'Champion zone turf'),
    ('Lakx turf', 'Lakx turf'),

]

SLOT_CHOICES = [
    ('9-11', '9:00 AM to 11:00 AM'),
    ('11-1', '11:30 AM to 1:00 PM'),
    ('1-3', '1:30 PM to 3:30 PM'),
    ('3-5', '3:30 PM to 5:30 PM'),
    ('5-7', '5:30 PM to 7:30 PM'),
    ('7-9', '7:30 PM to 9:30 PM'),
    ('9-12', '9:30 PM to 12:30 AM')
]

PAYMENT_CHOICES = [
    ('card', 'Credit/Debit Card'),
    ('upi', 'UPI'),
    ('cash', 'Cash'),
]




class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['team_name', 'turf', 'slot', 'is_tournament', 'tournament_name', 'payment_method']

        is_tournament = forms.ChoiceField(
        choices=[('yes', 'Yes'), ('no', 'No')],
        widget=forms.RadioSelect
        )
    slot = forms.ChoiceField(choices=SLOT_CHOICES)
    payment_method=forms.ChoiceField(choices=PAYMENT_CHOICES)


    def clean(self):
        cleaned_data = super().clean()
        is_tournament = cleaned_data.get('is_tournament')
        tournament_name = cleaned_data.get('tournament_name')

        if is_tournament == 'yes' and not tournament_name:
            self.add_error('tournament_name', 'Please enter the tournament name.')

        return cleaned_data


from django import forms
from .models import QuickMessage

class QuickMessageForm(forms.ModelForm):
    class Meta:
        model = QuickMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email', 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your Message', 'class': 'form-control', 'rows': 5}),
        }





