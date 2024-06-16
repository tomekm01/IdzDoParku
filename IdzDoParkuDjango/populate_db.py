# populate_db.py
import os
import django
from django.contrib.auth.hashers import make_password

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IdzDoParkuDjango.settings')
django.setup()

from main.models import Park, POI, Achievement, UserAchievement, User

def clear_database():
    # Usuń wszystkie obiekty z modeli
    UserAchievement.objects.all().delete()
    User.objects.all().delete()
    Achievement.objects.all().delete()
    POI.objects.all().delete()
    Park.objects.all().delete()

def populate():
    # Dodaj Park Południowy
    park_poludniowy = Park.objects.create(
        park_name="Park Południowy",
        location="Wrocław, Poland",
        description="Park Południowy to duży park miejski we Wrocławiu, znany ze swoich pięknych krajobrazów i licznych stawów."
    )

    # Dodaj Taras widokowy nad stawem w Parku Południowym
    POI.objects.create(
        park=park_poludniowy,
        name="Taras widokowy nad stawem",
        description="Piękny taras widokowy, skąd można podziwiać staw i otaczającą przyrodę.",
        latitude=51.0704,
        longitude=17.0217,
        qr_code="QR_CODE_LINK",
        additional_info_link="https://example.com",
        score_worth=10
    )

    first_ach = Achievement.objects.create(
        name="Dobry początek!",
        description="Gdzieś trzeba zacząć",
        requirements="Zdobądź pierwszy POI"
    )

    Achievement.objects.create(
        name="Pięć POI!",
        description="Dobrze idzie",
        requirements="Zdobądź 5 POI"
    )

    Agata = User.objects.create(
        username="Agata",
        password_hash=make_password("agataparks"),
        email="agata@gmail.com",
        score=10
    )

    UserAchievement.objects.create(
        user=Agata,
        achievement=first_ach
    )

if __name__ == '__main__':
    clear_database()
    populate()
