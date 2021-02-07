"""A vaccination calculator."""

__author__ = "730368118"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


Population: int = int(input("Population: "))sss
Doses_administered: int = int(input("Dose administered: "))
Doses_per_day: int = int(input("Doses per day: "))
Target_percent_vaccinated: int = int(input("Target percent vaccinated: "))
function: int= round((((Target_percent_vaccinated*(Population*2))/100) - Doses_administered)/Doses_per_day)
vaccination_daysleft: timedelta= timedelta(function)
today: datetime = datetime.today()
Vaccination_End_Days: datetime = today + vaccination_daysleft
Finish_date: str= Vaccination_End_Days.strftime("%B %d, %Y")
print( "We will reach " + str(Target_percent_vaccinated) + "% vaccination in " + str(function) + " days, which falls on " + Finish_date)
