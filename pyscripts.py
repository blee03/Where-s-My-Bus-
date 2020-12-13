
import http.client, urllib.request, urllib.parse, urllib.error, base64, json

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '617aa4d77c8b4d6e972688da30f0ea01',
}

params = urllib.parse.urlencode({
    '$format': 'json'
})
#grab route data
def grab_routes():
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
        if temp[0][i]['RouteId'].startswith('Ho') and temp[0][i]['RouteType'] == 'Bus':
            routeID.append(temp[0][i]['RouteId'])
            routeName.append(temp[0][i]['LongName'])
    return routeName
#ask for specific route

#val = (int(input("Input RouteID (numberical values only, starting from 0:"+((str(len(routeID)-1)) if len(routeID) > 0 else '0'))))
#print("RouteId: "+routeID[val])
#print("RouteId: "+routeName[val])
#callroute = routeID[val]
#grab stop data for specific route

def grab_stops(callroute):

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
#val = int(input("Input StopID (numberical values only, starting from 0:"+((str(len(StopID)-1)) if len(StopID) > 0 else '0')))
#callstop = StopID[0]
#print("Name: "+StopName[val])
#print("StopId: "+StopID[val])
#print("Latitude: "+str(Lat[val]))
#print("Longitude: "+str(Lon[val]))
#grab routes coming through given stop
try:
    conn = http.client.HTTPSConnection('hacktj2020api.eastbanctech.com')
    conn.request("GET", "/transitiq/Stops('"+callstop+"')/Routes?%s" % params, "{body}", headers)
    response = conn.getresponse()
    rfs = response.read()
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
#check for
temp = []
#print(rfs)
input_dict = json.loads(rfs)
for keyVal in input_dict:
    if isinstance(input_dict[keyVal], list):
        temp.append(input_dict[keyVal])
#isolate routes
rfsID = []
temp2 = temp[0]
for i in range(0, len(temp2)):
    if temp[0][i]['RouteId'].startswith('Ho'):
        rfsID.append(temp[0][i]['RouteId'])
#grab vehicle data
#print(rfsID)
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
#vehicle dictionary for index in original vehicle data
vehicle_dict = {}
count = 0
for i in range(0, len(temp[0])):
    vehicle_dict[(temp[0][i]['RouteId'])] = count
    count += 1

eta_dict = {}
for ID in rfsID:
    current_time = temp[0][vehicle_dict[ID]]['VehicleReportTime']
    
    params = urllib.parse.urlencode({
    # Request parameters
        '$format': 'json',
    })
    try:
        conn = http.client.HTTPSConnection('hacktj2020api.eastbanctech.com')
        conn.request("GET", "/transitiq/Stops('%s')/Arrivals?%s" % (StopID[val], params), "{body}", headers)
        response = conn.getresponse()
        arrival_data = response.read()
        #print(arrivals)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
    arrivals = []
    input_dict = json.loads(arrival_data)
    for keyVal in input_dict:
        if isinstance(input_dict[keyVal], list):
            arrivals.append(input_dict[keyVal])
    print(arrivals)
    for i in range(0, len(arrivals[0])):
        if arrivals[0][i]['RouteId'] == ID:
            temp_time = arrivals[0][i]['ScheduledTime']
    
    eta_dict[temp[0][vehicle_dict[ID]]['DestinationName']] = temp_time

#print(eta_dict)
