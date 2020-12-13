import http.client, urllib.request, urllib.parse, urllib.error, base64, json

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '617aa4d77c8b4d6e972688da30f0ea01',
}

params = urllib.parse.urlencode({
    '$format': 'json'
})
#grab route data
try:
    conn = http.client.HTTPSConnection('hacktj2020api.eastbanctech.com')
    conn.request("GET", "/transitiq/Routes?%s" % params, "{body}", headers)
    response = conn.getresponse()
    routedata = response.read()
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
#check for
temp = []
input_dict = json.loads(routedata)
for keyVal in input_dict:
    if isinstance(input_dict[keyVal], list):
        temp.append(input_dict[keyVal])
#isolate routes
routeID = []
routeName = []
temp2 = temp[0]
for i in range(0, len(temp2)):
    if temp[0][i]['RouteId'].startswith('Ho'):
        routeID.append(temp[0][i]['RouteId'])
        routeName.append(temp[0][i]['LongName'])
#ask for specific route
val = (int(input("Input RouteID (numberical values only, starting from 0: ")))
print("RouteId: "+routeID[val])
print("RouteId: "+routeName[val])
callroute = routeID[val]
#grab stop data for specific route
x = "/transitiq/Routes('"
y = "')/Stops?%s"
try:
    conn = http.client.HTTPSConnection('hacktj2020api.eastbanctech.com')
    conn.request("GET", x+callroute+y % params, "{body}", headers)
    response = conn.getresponse()
    stopdata = response.read()
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
    
#check for
temp = []
input_dict = json.loads(stopdata)
for keyVal in input_dict:
    if isinstance(input_dict[keyVal], list):
        temp.append(input_dict[keyVal])
#isolate lat values for all stops
Lat = []
temp2 = temp[0]
for i in range(0, len(temp2)):
    Lat.append(temp[0][i]['Lat'])
#isolate lon values for all stops
Lon = []
for x in range(0, len(temp2)):
    Lon.append(temp[0][x]['Lon'])
#isolate stopID for alls stops
StopID = []
for i in range(0, len(temp2)):
    StopID.append(temp[0][i]['StopId'])
#isolate name for alls stops
StopName = []
for i in range(0, len(temp2)):
    StopName.append(temp[0][i]['Name'])
#ask for specific stop
val = int(input("Input StopID (numberical values only, starting from 0: "))
callstop = StopID[val]
print("Name: "+StopName[val])
print("StopId: "+StopID[val])
print("Latitude: "+str(Lat[val]))
print("Longitude: "+str(Lon[val]))

x = "/transitiq/Routes('"
y = "')/Stops?%s"
try:
    conn = http.client.HTTPSConnection('hacktj2020api.eastbanctech.com')
    conn.request("GET", "/transitiq/Stops('{id}')/Routes?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))


#grab vehicle data
try:
    conn = http.client.HTTPSConnection('hacktj2020api.eastbanctech.com')
    conn.request("GET", "/transitiq/Vehicles?%s" % params, "{body}", headers)
    response = conn.getresponse()
    vehicledata = response.read()
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
#check for
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
#class vehicle definition
class vehicle:
    def __init__(self,iD):
        self.id = iD
v = []
vehicletemp = vehicle(vRouteID[0])
v.append(vehicletemp)
print(v)
vehicle_list = temp
#vehicle dictionary for index in original vehicle data
vehicle_dict = {}
count = 0
print(temp)
for i in range(0, len(temp[0])):
    vehicle_dict[(temp[0][i]['RouteId'])] = count
    count += 1
