# TempsEmoji 🌞
Aquest programa utilitza la llibreria Tweepy de Python per publicar tweets en un compte de Twitter amb el mapa del temps de Catalunya actual, utilitzant emojis per representar l'estat del temps.

![](https://nuvol.cat/temps_emoji.png)

## Requisits
- Una clau d'API d'OpenWeatherMap: Aquesta es pot obtenir gratuïtament des de [OpenWeatherMap](https://openweathermap.org/api)
- Una clau d'API de Twitter: Es pot obtenir des de [Twitter Developers](https://developer.twitter.com/)
- Python 3 instal·lat en l'ordinador
- Les llibreries `tweepy`,`requests` i `json`

## Utilització
1. Inserir les claus d'API d'OpenWeatherMap i Twitter a les variables corresponents al codi.
2. Executar el programa utilitzant python3.
3. El programa es repeteix cada 4 hores i publica un nou tweet amb les dades actualitzades.

## Nota
- Els codis postals de Catalunya utilitzats per obtenir les dades del temps estan en la variable `c`. Si es volen afegir o eliminar codis postals, aquesta variable s'ha de modificar.
- El programa pot ser modificat per publicar tweets amb una freqüencia diferent.

Aquest codi està disponible sota la llicència MIT. Utilitzeu-lo a voluntat i si us plau, no oblideu citar la font
