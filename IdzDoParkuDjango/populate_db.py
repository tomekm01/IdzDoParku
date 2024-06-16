import os
import django
from django.contrib.auth.hashers import make_password

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IdzDoParkuDjango.settings')
django.setup()

from main.models import Park, POI, Achievement, UserAchievement, User

def populate():
    # Dodaj Park Południowy
    park_poludniowy, created = Park.objects.get_or_create(
        park_name="Park Południowy",
        defaults={
            'location': "Wrocław, Poland",
            'description': "Park Południowy to duży park miejski we Wrocławiu, znany ze swoich pięknych krajobrazów i licznych stawów."
        }
    )

    # Dodaj Taras widokowy nad stawem w Parku Południowym
    POI.objects.get_or_create(
        park=park_poludniowy,
        name="Taras widokowy nad stawem",
        defaults={
            'description': "Piękny taras widokowy, skąd można podziwiać staw i otaczającą przyrodę.",
            'latitude': 51.0704,
            'longitude': 17.0217,
            'qr_code': "QR_CODE_LINK",
            'additional_info_link': "https://example.com",
            'score_worth': 10
        }
    )

    first_ach, created = Achievement.objects.get_or_create(
        name="Dobry początek!",
        defaults={
            'description': "Gdzieś trzeba zacząć",
            'requirements': "Zdobądź pierwszy POI"
        }
    )

    Achievement.objects.get_or_create(
        name="Pięć POI!",
        defaults={
            'description': "Dobrze idzie",
            'requirements': "Zdobądź 5 POI"
        }
    )

    Agata, created = User.objects.get_or_create(
        username="Agata",
        defaults={
            'password': make_password("agataparks"),
            'email': "agata@gmail.com"
        }
    )

    UserAchievement.objects.get_or_create(
        user=Agata,
        achievement=first_ach
    )

if __name__ == '__main__':
    populate()
