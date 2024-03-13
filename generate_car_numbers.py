import itertools
import random

def generate_car_numbers(count=10):
    letters = "АВЕКМНОРСТУХ"  # Subset of Cyrillic letters
    digits = "0123456789"
    
    # All region codes
    regions = [
        "01", "02", "102", "702", "03", "04", "05", "06", "07", "08", "09",
        "10", "11", "12", "13", "14", "15", "16", "116", "716", "17", "18",
        "19", "21", "121", "22", "23", "93", "123", "193", "24", "124", "25",
        "125", "26", "126", "27", "28", "29", "30", "31", "32", "33", "34",
        "134", "35", "36", "136", "37", "38", "138", "39", "40", "41", "42",
        "142", "43", "44", "45", "46", "47", "147", "48", "49", "50", "90",
        "150", "190", "750", "51", "52", "152", "53", "54", "154", "55", "56",
        "156", "57", "58", "59", "159", "60", "61", "161", "761", "62", "63",
        "163", "763", "64", "164", "65", "66", "96", "196", "67", "68", "69",
        "70", "71", "72", "73", "173", "74", "174", "75", "76", "77", "97",
        "99", "177", "197", "199", "777", "797", "799", "78", "98", "178",
        "198", "79", "82", "83", "86", "186", "87", "89", "92", "95"
    ]

    # Generate combinations for the car number parts
    first_part_letter = [l for l in letters]  # Single letters for the first part
    last_part_letters = [''.join(pair) for pair in itertools.product(letters, repeat=2)]
    digit_combinations = [''.join(triple) for triple in itertools.product(digits, repeat=3)]

    car_numbers = []
    for _ in range(count):
        fpl = random.choice(first_part_letter)
        dc = random.choice(digit_combinations)
        lpl = random.choice(last_part_letters)
        region = random.choice(regions)
        car_number = f"{fpl}{dc}{lpl}{region}"
        car_numbers.append(car_number)

    return car_numbers
