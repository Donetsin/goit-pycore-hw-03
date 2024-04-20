"""Module providing a function."""
import re

def normalize_phone(phone_number):
    """Finction formating phone number"""
    cleaned = re.sub(r"[^\d+]", "", phone_number)
    
    # add plus and/or country code
    if cleaned.startswith("380"):
        return "+" + cleaned
    elif not cleaned.startswith("+38"):
        return "+38" + cleaned
    else:
        return cleaned