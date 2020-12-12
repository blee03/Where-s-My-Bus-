import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '}',
}

params = urllib.parse.urlencode({
    # Request parameters
    'lat1': '{string}',
    'lon1': '{string}',
    'lat2': '{string}',
    'lon2': '{string}',
    '$format': '{String}',
    '$orderby': '{String}',
    'endTime': '{string}',
})

try:
    conn = http.client.HTTPSConnection('hacktj2020api.eastbanctech.com')
    conn.request("GET", "/transitiq/CalculateItineraryArrivingAt?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))



print('hello brian')
