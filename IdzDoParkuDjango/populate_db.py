# populate_db.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IdzDoParkuDjango.settings')
django.setup()

from main.models import Park, POI

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

if __name__ == '__main__':
    populate()
