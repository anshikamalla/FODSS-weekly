
"""
Description:
    This module defines a function called add_daily_temp which accepts:
      - a dictionary to hold average daily temperatures,
      - a temperature value,
      - a day of the week.
    The function adds the temperature to the dictionary only if that day is not already present,
    and returns the updated dictionary.
"""

def add_daily_temp(temps_dict, temp, day):
    # Add temperature if day is not already in the dictionary
    if day not in temps_dict:
        temps_dict[day] = temp
    return temps_dict

if __name__ == "__main__":
    # Example usage
    daily_temps = {}
    # Sample calls (or you can prompt the user)
    daily_temps = add_daily_temp(daily_temps, 75.5, "Monday")
    daily_temps = add_daily_temp(daily_temps, 80.0, "Tuesday")
    # Attempting to add temperature for Monday again (should not update)
    daily_temps = add_daily_temp(daily_temps, 78.0, "Monday")
    print("Daily Temperatures:", daily_temps)
