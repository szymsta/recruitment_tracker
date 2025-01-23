
import requests
import pprint
import credentials
"""
application/x-www-form-urlencoded - mówi o tym że dane są przesyłane jako klucz wartoć 
application/json - mówi że dane są przesyłane w formie JSON
"""
# Wykonanie żądania POST
response = requests.post(credentials.url, headers = credentials.headers, data=credentials.data)

# Sprawdzenie odpowiedzi
if response.status_code == 200:
    token = response.json()['access_token']
    print("Odpowiedź:", token)  # Wyświetl odpowiedź JSON
else:
    print(f"Błąd: {response.status_code}, {response.text}")
    
