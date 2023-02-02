# Импортируется json file из внешнего источника
import requests as requests

URL = "https://www.jsonkeeper.com/b/0MZI"

result = requests.get(URL).json()
