# populate_db.py
import datetime
import os
import django
from django.contrib.auth.hashers import make_password

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IdzDoParkuDjango.settings')
django.setup()

from main.models import Park, POI, Achievement, UserAchievement, User, LoginSession, QRScan, Comment

def clear_database():
    # Usuń wszystkie obiekty z modeli
    Comment.objects.all().delete()
    QRScan.objects.all().delete()
    LoginSession.objects.all().delete()
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
        qr_code="poludniowytaras",
        additional_info_link="https://example.com",
        score_worth=10
    )

    # Dodaj Park Szczytnicki
    park_szczytnicki = Park.objects.create(
        park_name="Park Szczytnicki",
        location="Wrocław, Poland",
        description="Leśny park ze słynnym ogrodem japońskim zaprojektowanym w 1913 r. i kilkakrotnie później przebudowywanym."
    )

    POI.objects.create(
        park=park_szczytnicki,
        name="Aleja Sakur",
        description="Wyjątkowy sad z oryginalnymi drzewkami japońskich wiśni",
        latitude=51.1141, 
        longitude=17.0783,
        qr_code="szczytsakur",
        additional_info_link="https://example.com",
        score_worth=10
    )

    POI.objects.create(
        park=park_szczytnicki,
        name="Pomnik Schillera",
        description="Pomnik przedstawiający niemieckiego literata Friedricha Schillera",
        latitude=51.1133,
        longitude=17.0831,
        qr_code="szczytschill",
        additional_info_link="https://example.com",
        score_worth=10
    )

    POI.objects.create(
        park=park_szczytnicki,
        name="Altana",
        description="Jest to rekonstrukcja miedzianej altany, która wcześniej znajdowała się w tym miejscu. ",
        latitude=51.1139,
        longitude=17.0885,
        qr_code="szczytaltana",
        additional_info_link="https://example.com",
        score_worth=10
    )

    # Dodaj Park Juliusza Słowackiego
    park_slowackiego = Park.objects.create(
        park_name="Park Juliusza Słowackiego",
        location="Wrocław, Poland",
        description="Spokojny park miejski pełen posągów i pomników wojennych nazwany na cześć polskiego poety romantycznego."
    )

    POI.objects.create(
        park=park_slowackiego,
        name="Pomnik Juliusza Słowackiego",
        description="Pomnik upamiętniający polskiego wieszcza narodowego – Juliusza Słowackiego.",
        latitude=51.1093,
        longitude=17.0452,
        qr_code="slowakpomnik",
        additional_info_link="https://example.com",
        score_worth=10
    )

    POI.objects.create(
        park=park_slowackiego,
        name="Rzeźba \"Oczekiwanie\"",
        description="Przedstawia dwa duże fotele, mocno stylizowane, sprawiające wrażenie miękkich i wygodnych. Na jednym siedząca postać młodej kobiety w okularach i sukience.",
        latitude=51.1101,
        longitude=17.0476,
        qr_code="slowakrzezba",
        additional_info_link="https://example.com",
        score_worth=10
    )

    # Dodaj Park Zachodni
    park_zachodni = Park.objects.create(
        park_name="Park Zachodni",
        location="Wrocław, Poland",
        description="Zielony park miejski z placami zabaw dla dzieci i pozostałościami po fortyfikacjach z czasów I wojny światowej."
    )

    POI.objects.create(
        park=park_zachodni,
        name="Schron Piechoty I.R.-10",
        description="Schron piechoty typu magazynowego wybudowany w latach 1895-96.",
        latitude=51.1318,
        longitude=16.9675,
        qr_code="zachodnischron",
        additional_info_link="https://example.com",
        score_worth=10
    )

    POI.objects.create(
        park=park_zachodni,
        name="Pomnik Anioła",
        description="Figura anioła z urną we wrocławskim Parku Zachodnim przypomina, że utworzony w latach 1905-1910 park był powiązany z cmentarzami.",
        latitude=51.1316,
        longitude=16.9769,
        qr_code="zachodnianiol",
        additional_info_link="https://example.com",
        score_worth=10
    )

    # Dodaj Park Wschodni
    park_wschodni = Park.objects.create(
        park_name="Park Wschodni",
        location="Wrocław, Poland",
        description="Położony nad rzeką rozległy park z terenami trawiastymi i kładkami – malownicze miejsce na spacery."
    )

    mala_niagara = POI.objects.create(
        park=park_wschodni,
        name="Mała \"Niagara\"",
        description="Kaskada wodna na wschodnim krańcu parku",
        latitude=51.0858,
        longitude=17.0904,
        qr_code="wschodnipomnik",
        additional_info_link="https://example.com",
        score_worth=10
    )

    POI.objects.create(
        park=park_wschodni,
        name="Megafony",
        description="Instalacja akustyczna do wzmacniania dźwięków krajobrazu, składająca się oryginalnie z trzech, aktualnie – ze względów konserwatorskich – z dwóch olbrzymich drewnianych megafonów, zbudowanych przez studentów architektury wnętrz Estońskiej Akademii Sztuki",
        latitude=51.0866,
        longitude=17.0866,
        qr_code="wschodnimegafon",
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

    agata = User.objects.create(
        username="Agata",
        password_hash=make_password("agataparks"),
        email="agata@gmail.com",
        score=10
    )

    QRScan.objects.create(
        poi=mala_niagara,
        user=agata,
        scan_date=datetime.datetime.now()
    )

    UserAchievement.objects.create(
        user=agata,
        achievement=first_ach
    )

if __name__ == '__main__':
    clear_database()
    populate()
