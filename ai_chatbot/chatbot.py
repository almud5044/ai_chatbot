from orders import orders, products

def get_ai_response(user_message):
    """
    AI-simulator som svarer på spørsmål om ordre og produkter.
    """
    user_message_lower = user_message.lower()

    # Hilsener
    if "hei" in user_message_lower or "hallo" in user_message_lower:
        return "Hei! Hvordan kan jeg hjelpe deg i dag?"

    # Ordre-status
    elif "ordre" in user_message_lower:
        for ordre_id in orders:
            if ordre_id in user_message:
                ordren = orders[ordre_id]
                return f"Ordre {ordre_id} er {ordren['status']} og produktet er {ordren['produkt']}. Leveringsdato: {ordren['leveringsdato']}"
        return "Kan du oppgi ordrenummeret ditt?"

    # Produkttilgjengelighet
    elif "produkt" in user_message_lower:
        for produktnavn in products:
            if produktnavn.lower() in user_message_lower:
                p = products[produktnavn]
                lager_status = "tilgjengelig" if p["lager"] > 0 else "ikke tilgjengelig"
                return f"Produktet {produktnavn} er {lager_status}. Pris: {p['pris']} kr."
        return "Hvilket produkt spør du om?"

    # Takk
    elif "takk" in user_message_lower:
        return "Bare hyggelig! 😊"

    # Standard fallback
    else:
        return "Beklager, jeg forstår ikke helt. Kan du formulere spørsmålet på en annen måte?"
