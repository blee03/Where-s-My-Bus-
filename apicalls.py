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
    if Type == '1':
        return routeName
    if Type == '2':
        return routeID
