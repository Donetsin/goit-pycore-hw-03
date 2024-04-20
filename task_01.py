"""Module providing a function."""
from datetime import datetime as dt

def get_days_from_today(date):
    """Function printing difference in days bewteen current and inputted date."""
    # convert inputted date from string to type datetime
    try:
        given_date = dt.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        print(f'The {date} is not a valid date. Please input the date in the format YYYY-MM-DD')
        return None
    except BaseExceptionGroup:
        print(f'Error: {BaseExceptionGroup}')
        return None
    
    # get current date
    current_date = dt.today().date()

    # calculate difference between current and inputted date
    delta = current_date - given_date

    # return difference in days
    return delta.days
