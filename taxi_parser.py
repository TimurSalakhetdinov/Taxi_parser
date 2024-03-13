import requests
import sys

def get_car_info(car_number):
    """
    Получает информацию о машине по номеру автомобиля, используя API.

    Args:
    car_number (str): Номер машины для запроса информации.

    Returns:
    dict: Информация о машине в виде словаря, если запрос успешен, иначе сообщение об ошибке.
    """
    car_number_encoded = requests.utils.quote(car_number)
    url = f"https://szlt.sicmt.ru/external-car/api/car?regNumTS={car_number_encoded}"

    headers = {
        'accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    }
    
    response = requests.get(url, headers=headers, verify=False)

    if response.status_code == 200:
        return response.json()
    else:
        return f"Ошибка {response.status_code}: {response.text}"

def format_for_database(car_info):
    """
    Форматирует полученную информацию о машине для вставки в базу данных.

    Args:
    car_info (list): Список с информацией о машине, полученный от API.

    Returns:
    dict: Словарь с данными машины, подготовленными для базы данных, или None, если информация отсутствует.
    """
    if car_info and isinstance(car_info, list) and car_info:
        car = car_info[0]  # Предполагается, что первый элемент списка содержит информацию о нужной машине
        
        car_data_for_db = {
            "license_number": car.get('licenseNumber'),
            "license_start_date": car.get('licenseStartDate'),
            "vehicle_brand": car.get('vehicleBrand'),
            "vehicle_model": car.get('vehicleModel'),
            "vehicle_year": car.get('vehicleYear'),
            "vehicle_colour": car.get('vehicleColour', 'Н/Д'),  # 'Н/Д' используется по умолчанию, если поле 'vehicleColour' отсутствует
            "license_status": car.get('licenseStatus'),
            "region_name": car.get('regionName')
        }
        return car_data_for_db
    else:
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python taxi_parser.py <номер_машины>")
        sys.exit(1)

    car_number = sys.argv[1]
    car_info = get_car_info(car_number)
    car_data_for_db = format_for_database(car_info)

    if car_data_for_db:
        print(car_data_for_db)
        # Здесь должен быть ваш код для вставки 'car_data_for_db' в базу данных
        # Например: insert_into_database(car_data_for_db)
    else:
        print("Данные по указанному номеру машины отсутствуют или произошла ошибка.")
