import requests
import json
def saa_tila(paikkakunta, api_key):
    try:
        url=f"http://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid={api_key}"
        response=requests.get(url)
        response.raise_for_status()
        data=response.json()

        kelvin=data["main"]["temp"]
        celsius=kelvin-273
        saa_kuvaus=data["weather"][0]["description"]

        return f"Sää paikkakunnalla {paikkakunta}: {saa_kuvaus.capitalize()}, lämpötila: {celsius:.1f} C"
    except requests.exceptions.RequestException as e:
        return f"Säätietojen hakeminen epäonnistui: {e}"

if __name__=="__main__":
    paikkakunta=input("Anna paikkakunta: ")
    api_key="dd786fd2e4de30ee612b9ab3aa8140fd"
    print(saa_tila(paikkakunta, api_key))





