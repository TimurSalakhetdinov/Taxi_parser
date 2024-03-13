def format_for_database(car_info, car_number):
    # Default data structure in case of no license or API errors
    default_data = {
        "car_number": car_number,
        "license_number": "no license",
        "license_start_date": "NA",
        "vehicle_brand": "NA",
        "vehicle_model": "NA",
        "vehicle_year": "NA",
        "license_status": "NA",
        "region_name": "NA"
    }

    if car_info and isinstance(car_info, list) and car_info:
        car = car_info[0]  # Assuming the first item contains the car's data
        car_data_for_db = {
            "car_number": car_number,
            "license_number": car.get('licenseNumber', 'no license'),
            "license_start_date": car.get('licenseStartDate', 'NA'),
            "vehicle_brand": car.get('vehicleBrand', 'NA'),
            "vehicle_model": car.get('vehicleModel', 'NA'),
            "vehicle_year": car.get('vehicleYear', 'NA'),
            "license_status": car.get('licenseStatus', 'NA'),
            "region_name": car.get('regionName', 'NA')
        }
        return car_data_for_db
    else:
        return default_data
