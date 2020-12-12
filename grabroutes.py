import http.client, urllib.request, urllib.parse, urllib.error, base64, json

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '617aa4d77c8b4d6e972688da30f0ea01',
}

params = urllib.parse.urlencode({
    '$format': 'json'
})

try:
    conn = http.client.HTTPSConnection('hacktj2020api.eastbanctech.com')
    conn.request("GET", "/transitiq/Routes?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    #print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))


print(data[0])
keyVal = 'RouteId'
routeID = []
input_dict = json.loads(data)
for keyVal in input_dict:
    if isinstance(input_dict[keyVal], list):
        routeID.append(input_dict[keyVal])

temp = []
for i in range(0, len(routeID)):
    temp.append(routeID[i][0])
print(routeID)
print(temp)
