import requests

from config.config import BASE_URL, HEADERS
from utils.logger import get_logger

logger = get_logger()

def get(endpoint):
    logger.info(f"GET request to {BASE_URL}{endpoint}")
    response = requests.get(f"{BASE_URL}{endpoint}", headers=HEADERS)
    logger.info(f"GET response: {response.status_code}")
    return response

def post(endpoint, payload):
    logger.info(f"POST request to {BASE_URL}{endpoint}")
    response = requests.post(f"{BASE_URL}{endpoint}", json=payload, headers=HEADERS)
    logger.info(f"POST response: {response.status_code}")
    return response

def put(endpoint, payload):
    logger.info(f"PUT request to {BASE_URL}{endpoint}")
    response = requests.put(f"{BASE_URL}{endpoint}", json=payload, headers=HEADERS)
    logger.info(f"PUT response: {response.status_code}")
    return response

def delete(endpoint):
    logger.info(f"DELETE request to {BASE_URL}{endpoint}")
    response = requests.delete(f"{BASE_URL}{endpoint}", headers=HEADERS)
    logger.info(f"DELETE response: {response.status_code}")
    return response

