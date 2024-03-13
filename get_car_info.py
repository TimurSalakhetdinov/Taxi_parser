import requests
import logging

def get_car_info(car_number):
    logging.basicConfig(level=logging.INFO)
    try:
        car_number_encoded = requests.utils.quote(car_number)
        url = f"https://szlt.sicmt.ru/external-car/api/car?regNumTS={car_number_encoded}"

        headers = {
            'accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, verify=False)  # Consider adding SSL certificate verification for security

        if response.status_code == 200:
            return response.json()
        else:
            logging.error(f"Error {response.status_code}: {response.text}")
            return None
    except Exception as e:
        logging.error(f"Exception occurred: {e}")
        return None