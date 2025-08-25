# orders.py - Fiktiv database over ordrer og produkter
orders = {
    "1001": {"status": "Sendt", "produkt": "Laptop", "leveringsdato": "28. aug 2025"},
    "1002": {"status": "Behandles", "produkt": "Mobiltelefon", "leveringsdato": "31. aug 2025"},
    "1003": {"status": "Avslått", "produkt": "Headset", "leveringsdato": None},
}

products = {
    "Laptop": {"lager": 5, "pris": 15000},
    "Mobiltelefon": {"lager": 0, "pris": 8000},
    "Headset": {"lager": 12, "pris": 1200},
}
