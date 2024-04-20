"""Module providing a function."""
from datetime import datetime as dt, timedelta as td

def get_upcoming_birthdays(users):
    """Returns list of employee Birthday during next 7 days"""
    current_date = dt.today().date()
    birthdays = []

    for user in users:
        birthday = dt.strptime(user["birthday"], "%Y.%m.%d").date()
        this_year_birthday = birthday.replace(year = current_date.year)
        
        # birthday has already passed
        if this_year_birthday < current_date:
            # use next year birthday
            this_year_birthday = this_year_birthday.replace(year = current_date.year + 1) 
    
        days_delta = (this_year_birthday - current_date).days
        # check if birthday in next 7 days
        if 0 <= days_delta <= 7:
            # if Saturday or Sunday
            if this_year_birthday.weekday() >= 5:
                # move to Monday
                this_year_birthday += td(days = (7 - this_year_birthday.weekday()))
        
            # populate birthday greetings
            birthdays.append({"name": user["name"], "congratulation_date": this_year_birthday.strftime("%Y.%m.%d")})

    return birthdays