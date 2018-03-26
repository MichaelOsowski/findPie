from flask import Flask
from flask import jsonify
import socket
import fcntl
import struct

def getIP(ifname):

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ipaddr = socket.inet_ntoa(fcntl.ioctl(
         s.fileno(),
         0x8915,  # SIOCGIFADDR
         struct.pack('256s', ifname[:15])
                )[20:24])
        hostname = socket.gethostname()
        return ipaddr
    except:
        pass

app=Flask(__name__)

@app.route("/")
def main():

    outDict = {}
    myeth=getIP('eth0')
    mywlan=getIP('wlan0')
    hostname = socket.gethostname()
    outDict['host'] = hostname;
    outDict['wired'] = myeth;
    outDict['wireless'] = mywlan;
    return jsonify(outDict)

app.run(host='0.0.0.0')
if __name__ == "__main__":
        app.run()