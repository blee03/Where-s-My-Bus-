########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '0466719b080e49999811b70f9cd28e85',
}

params = urllib.parse.urlencode({
    # Request parameters
    '$filter': '{String}',
    '$top': '{string}',
    '$skip': '{string}',
    '$format': '{String}',
    '$orderby': '{String}',
})

try:
    conn = http.client.HTTPSConnection('hacktj2020api.eastbanctech.com')
    conn.request("GET", "/transitiq/Stops?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
