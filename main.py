import tweepy, requests, json, time

# API key per a OpenWeatherMap
api_key = ""

# Autentificació a Twitter
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
bearer_token = ""

client = tweepy.Client( bearer_token=bearer_token, 
                        consumer_key=consumer_key, 
                        consumer_secret=consumer_secret, 
                        access_token=access_token, 
                        access_token_secret=access_token_secret, 
                        return_type = requests.Response,
                        wait_on_rate_limit=True)


# Llista de codis postals en l'ordre del mapa

c = ['25550', '25598', '25595', '25580', '25527', '25597', '25572', '25700', '17538', '17534', '17868', '17733', '17700', '17488', '22584', '25560', '25794', '25717', '08695', '08696', '17500', '17857', '17820', '17130', '25632', '25631', '25790', '25282', '08600', '08513', '08500', '17430', '17003', '17250', '25691', '25735', '25749', '25287', '08670', '08180', '08540', '17401', '17320', '25600', '25335', '25200', '08281', '08241', '08146', '08182', '08301', '25002', '25230', '25340', '43427', '08700', '08784', '08172', '08025', '25179', '25177', '25440', '43800', '43717', '08870', '08860', '43730', '43772', '43204', '43110', '43006', '43780', '43750', '43746', '43528', '43500', '43895', '43560', '43580']
e = []

def mapa():
    for zip in c:

        # Solicitud API per saber el temps
        response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={zip},es&appid={api_key}")

        # Analitzem la resposta JSON
        data = json.loads(response.text)

        # Definim un diccionari d'emojis
        emoji_dict = {
            "01d": "☀️",
            "02d": "🌤",
            "03d": "☁️",
            "04d": "☁️",
            "09d": "🌧",
            "10d": "🌦",
            "11d": "⛈️",
            "13d": "❄️",
            "50d": "🌫",
            "01n": "🌕",
            "02n": "🌤",
            "03n": "☁️",
            "04n": "☁️",
            "09n": "🌧",
            "10n": "🌦",
            "11n": "⛈️",
            "13n": "❄️",
            "50n": "🌫"
        }

        # Obtenim l'icona de OpenWeatherMap
        condition_icon = data["weather"][0]["icon"]

        # Transformem l'icona a emoji
        emoji = emoji_dict.get(condition_icon, "❔")

        # Afegim l'emoji a la llista
        e.append(emoji)

    # Definim una funció per crear segments d'emoji
    def sgm(n):
        s = ""
        for i in range(n):
            s += e.pop(0)
        return(s+"\n")

    # Dibuixem el mapa de Catalunya utilitzant els segments
    return(sgm(4)+sgm(10)+sgm(10)+sgm(10)+sgm(9)+sgm(8)+sgm(8)+sgm(7)+sgm(5)+sgm(3)+sgm(2)+sgm(2))

while True:
    # Tuitem el contingut
    client.create_tweet(text=mapa())
    # Esperem 4 hores
    time.sleep(4 * 60 * 60)