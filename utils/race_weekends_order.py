race_order_2022 = {
    1: 'Bahrain',
    2: 'Saudi Arabia',
    3: 'Australia',
    4: 'Emilia Romagna',
    5: 'Miami',
    6: 'Spain',
    7: 'Monaco',
    8: 'Azerbaijan',
    9: 'Canada',
    10: 'Great Britain',
    11: 'Austria',
    12: 'France',
    13: 'Hungary',
    14: 'Belgium',
    15: 'Netherlands',
    16: 'Italy',
    17: 'Singapore',
    18: 'Japan',
    19: 'United States',
    20: 'Mexico',
    21: 'Brazil',
    22: 'Abu Dhabi'
}

race_order_2023 = {
    1: 'Bahrain',
    2: 'Saudi Arabia',
    3: 'Australia',
    4: 'Azerbaijan',
    5: 'Miami',
    6: 'Monaco',
    7: 'Spain',
    8: 'Canada',
    9: 'Austria',
    10: 'Great Britain',
    11: 'Hungary',
    12: 'Belgium',
    13: 'Netherlands',
    14: 'Italy',
    15: 'Singapore',
    16: 'Japan',
    17: 'Qatar',
    18: 'United States',
    19: 'Mexico',
    20: 'Brazil',
    21: 'Las Vegas',
    22: 'Abu Dhabi'
}

race_order_2024 = {
    1: 'Bahrain',
    2: 'Saudi Arabia',
    3: 'Australia',
    4: 'Japan',
    5: 'China',
    6: 'Miami',
    7: 'Emilia Romagna',
    8: 'Monaco',
    9: 'Canada',
    10: 'Spain',
    11: 'Austria',
    12: 'Great Britain',
    13: 'Hungary',
    14: 'Belgium',
    15: 'Netherlands',
    16: 'Italy',
    17: 'Azerbaijan',
    18: 'Singapore',
    19: 'United States',
    20: 'Mexico',
    21: 'Brazil',
    22: 'Las Vegas',
    23: 'Qatar',
    24: 'Abu Dhabi'
}

race_orders = {
    2022: race_order_2022,
    2023: race_order_2023,
    2024: race_order_2024,
}

unique_races = []
for races in race_orders.values():
    for race in races.values():
        if race not in unique_races:
            unique_races.append(race)
unique_races.sort()