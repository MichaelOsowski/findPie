import sys
import urllib2
import json

print 'Starting Process'
for x in range(0, 1000):
    url = 'http://' + sys.argv[1] + '.' + str(x) + ':5000/'
    req = urllib2.Request(url)
    req.add_header('Accept', 'application/json')
    #print ('trying: ' + url )
    try:
        siteresponse=urllib2.urlopen(req,timeout = .1)
        response = siteresponse.read()
        jsonResponse = json.loads(response)
        print 'Hostname: ' + str(jsonResponse['host']) +' wireless: ' + str(jsonResponse['wireless']) + ' wired: ' + str(jsonResponse['wired'])
    except Exception:      
        pass
print 'Process Complete'
exit(0)