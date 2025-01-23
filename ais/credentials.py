
#link
url = "https://id.barentswatch.no/connect/token"

#kontent przesyłany jako para klucz-wartosc
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}


# Dane, autoryzacyjne w celu uzyskania tokenu
data = {
    "grant_type": "client_credentials",
    "client_id": "stasiur@gmail.com:stasiur", #mail:login
    "client_secret": "Analizadanych123", #hasło
    "scope": "ais"
}
