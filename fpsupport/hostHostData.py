import json
import requests

def hostInfo(InIPAddress,lastOctet):

    timeout = 500

    try:
        url = 'http://' + InIPAddress + '.' + str(lastOctet) + ':5000/'

        headers = {}
        headers['Accept'] = 'application/json'
        siteresponse = requests.get(url, headers=headers, timeout=timeout)
        #print(siteresponse.text)
        jsonResponse = json.loads(siteresponse.text)
        print('Hostname: ' + str(jsonResponse['host']) + ' wireless: ' + str(jsonResponse['wireless']) + ' wired: ' + str(jsonResponse['wired']))
    except:
        pass


