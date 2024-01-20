import http.client

conn = http.client.HTTPSConnection("spotify23.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "ece8d130bbmsh5f31791fa899f3ap16e494jsnfb9f94437e83",
    'X-RapidAPI-Host': "spotify23.p.rapidapi.com"
}

conn.request("GET", "/search/?q=%3CREQUIRED%3E&type=multi&offset=0&limit=10&numberOfTopResults=5", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))