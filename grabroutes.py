import http.client, urllib.request, urllib.parse, urllib.error, base64, json
def getRouteList():
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
        routeID.append(temp[0][i]['RouteId'])
    #print(routeID)
    return routeID

def getStopList(routeID):
    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': '617aa4d77c8b4d6e972688da30f0ea01',
    }
    params = urllib.parse.urlencode({
        # Request parameters
        '$format': 'json',
    })

    try:
        conn = http.client.HTTPSConnection('hacktj2020api.eastbanctech.com')
        conn.request("GET", "/transitiq/Routes(%s})/Stops?%s" % (routeID, params), "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
    
routes = getRouteList()
getStopList(routes[0])
