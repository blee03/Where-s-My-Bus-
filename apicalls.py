import http.client, urllib.request, urllib.parse, urllib.error, base64, json
headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '617aa4d77c8b4d6e972688da30f0ea01',
}

params = urllib.parse.urlencode({
    '$format': 'json'
})

#grab route data
def grab_routes(Type):
    routedata= []
    params = urllib.parse.urlencode({
        '$format': 'json'
    })
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
    route_dict = {}
    for i in range(0, len(temp[0])):
        if temp[0][i]['RouteId'].startswith('Ho') and temp[0][i]['RouteType'] == 'Bus':
            routeID.append(temp[0][i]['RouteId'])
            routeName.append(temp[0][i]['LongName'])
            route_dict[temp[0][i]['RouteId']] = temp[0][i]['LongName']
    if Type == '1':
        return routeName
    elif Type == '2':
        return routeID
    elif Type == '3':
        return route_dict
def grab_stops(val, Type):
    x = "/transitiq/Routes('"
    y = "')/Stops?%s"
    routeIDs = grab_routes("2")
    callroute = routeIDs[val]
    route_num = val
    params = urllib.parse.urlencode({
        '$format': 'json'
    })
    try:
        conn = http.client.HTTPSConnection('hacktj2020api.eastbanctech.com')
        conn.request("GET", x+callroute+y % params, "{body}", headers)
        response = conn.getresponse()
        stopdata = response.read()
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
#check for dicts    
    temp = []
    input_dict = json.loads(stopdata)
    for keyVal in input_dict:
        if isinstance(input_dict[keyVal], list):
            temp.append(input_dict[keyVal])

#isolate stopsIDS
    stopID = []
    stop_names = []
    temp2 = temp[0]
    for i in range(0, len(temp2)):
        stopID.append(temp[0][i]['StopId'])
        stop_names.append(temp[0][i]['Name'])

    if Type == '1':
        return stop_names, val
    elif Type == '2':
        return stopID, val

def bus_ETA(val, route_num):
    stopIDs = grab_stops(route_num, '2')[0]
    callstop = stopIDs[val]
    rfs = bytearray()
    params = urllib.parse.urlencode({
        '$format': 'json'
    })
    try:
        conn = http.client.HTTPSConnection('hacktj2020api.eastbanctech.com')
        conn.request("GET", "/transitiq/Stops('"+callstop+"')/Routes?%s" % params, "{body}", headers)
        response = conn.getresponse()
        rfs = response.read()
        conn.close()
        print(rfs)
    except Exception as e:
        print(e)

    temp = []
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
    route_dict = grab_routes('3')
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
            conn.request("GET", "/transitiq/Stops('%s')/Arrivals?%s" % (stopIDs[val], params), "{body}", headers)
            response = conn.getresponse()
            arrival_data = response.read()
            #print(arrivals)
            conn.close()
        except Exception as e:
            raise e
        
       
        arrivals = []
        print(arrivals)
        input_dict = json.loads(arrival_data)
        for keyVal in input_dict:
            if isinstance(input_dict[keyVal], list):
                arrivals.append(input_dict[keyVal])
        for i in range(0, len(arrivals[0])):
            if arrivals[0][i]['RouteId'] == ID:
                temp_time = arrivals[0][i]['ScheduledTime']
        
        eta_dict[route_dict[ID]] = temp_time

    return eta_dict
