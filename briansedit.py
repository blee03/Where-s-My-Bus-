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


temp = []
input_dict = json.loads(data)
for keyVal in input_dict:
    if isinstance(input_dict[keyVal], list):
        temp.append(input_dict[keyVal])

routeID = []
temp2 = temp[0]
for i in range(0, len(temp2)):
    if temp[0][i]['RouteId'].startswith('Ho'):
        routeID.append(temp[0][i]['RouteId'])

#call stop using id
callstop = str(routeID[0])

print(routeID)
print(callstop)

import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '617aa4d77c8b4d6e972688da30f0ea01',
}

params = urllib.parse.urlencode({
    # Request parameters
    '$format': 'json'

})
x = "/transitiq/Routes('"
y = "')/Stops?%s"
try:
    conn = http.client.HTTPSConnection('hacktj2020api.eastbanctech.com')
    conn.request("GET", x+callstop+y % params, "{body}", headers)
    response = conn.getresponse()
    stopdata = response.read()
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
    
#grab lat values
temp = []
input_dict = json.loads(stopdata)
for keyVal in input_dict:
    if isinstance(input_dict[keyVal], list):
        temp.append(input_dict[keyVal])

Lat = []
temp2 = temp[0]
for i in range(0, len(temp2)):
    Lat.append(temp[0][i]['Lat'])

#grab lon values
Lon = []
for x in range(0, len(temp2)):
    Lon.append(temp[0][x]['Lon'])
#print(Lat[0])
#print(Lon[0])
#print(Lat[1])
#print(Lon[1])

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '617aa4d77c8b4d6e972688da30f0ea01',
}

params = urllib.parse.urlencode({
})

try:
    conn = http.client.HTTPSConnection('hacktj2020api.eastbanctech.com')
    conn.request("GET", "/transitiq/Vehicles?%s" % params, "{body}", headers)
    response = conn.getresponse()
    vehicledata = response.read()
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
#loops through vehicledata
temp = []
input_dict = json.loads(vehicledata)
for keyVal in input_dict:
    if isinstance(input_dict[keyVal], list):
        temp.append(input_dict[keyVal])
temp2 = temp[0]
#checks vehicle lat
vLat = []
for i in range(0, len(temp2)):
    vLat.append(temp[0][i]['Latitude'])
#checks vehicle lon
vLon = []
for x in range(0, len(temp2)):
    vLon.append(temp[0][x]['Longitude'])
#checks vehicle route id
vRouteID = []
for z in range(0, len(temp2)):
    vRouteID.append(temp[0][z]['RouteId'])
print(vLat)
print(vLon)
print(vRouteID)
