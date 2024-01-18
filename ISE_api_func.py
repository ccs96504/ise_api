
import http.client
import base64
import ssl,json
import sys
import info



####
# info.py is in your ise_info
# info.py
# ip = "1.2.3.4"
# user = "admin"
# password = '12345678'
####

sys.argv.append(info.ip)
sys.argv.append(info.user)
sys.argv.append(info.password)

host = sys.argv[1] 
user = sys.argv[2]
password = sys.argv[3] 


conn = http.client.HTTPSConnection("{}:9060".format(host), context=ssl.SSLContext(ssl.PROTOCOL_TLSv1_2))

creds = str.encode(':'.join((user, password)))
encodedAuth = bytes.decode(base64.b64encode(creds))

headers = {
    'accept': "application/json",
    'authorization': " ".join(("Basic",encodedAuth)),
    'cache-control': "no-cache",
    }

class Endpoint_MAC:
    def __init__(self,MAC):
        self.mac = MAC
    def get_id (self):
        conn.request("GET", "/ers/config/endpoint/name/{}".format(self.mac), headers=headers)
        res = conn.getresponse()
        data = res.read()
        #print("Status: {}".format(res.status))
        #print("Header:\n{}".format(res.headers))
        #print("Body:\n{}".format(data.decode("utf-8")))

        if data.decode("utf-8")=='':
            return None
        else:
            Body_info = data.decode("utf-8")
            Body_info = json.loads(Body_info)
            id = Body_info['ERSEndPoint']['id']
        return id
    
    
    def delete (self):
        conn.request("DELETE", "/ers/config/endpoint/{}".format(self.get_id()) , headers=headers)
        res = conn.getresponse()
        data = res.read()


        print("Status: {}".format(res.status))
        if res.status == 404:
            print("no have mac {}".format(self.mac))
        elif res.status == 204:
            print('delete mac {}'.format(self.mac))
        else:
            print("Exception!!")

    def __str__(self) :
        return f"{self.mac}"
        
class internaluser:
    
    def __init__(self,MAC):
        self.mac = MAC
    def get_id (self):
        conn.request("GET", "/ers/config/internaluser/name/{}".format(self.mac), headers=headers)
        res = conn.getresponse()
        data = res.read()
        print("Status: {}".format(res.status))
        print("Header:\n{}".format(res.headers))
        print("Body:\n{}".format(data.decode("utf-8")))

        if data.decode("utf-8")=='':
            return None
        else:
            Body_info = data.decode("utf-8")
            Body_info = json.loads(Body_info)
            id = Body_info['InternalUser']['id']
        return id
    def delete (self):
        conn.request("DELETE", "/ers/config/internaluser/name/{}".format(self.mac) , headers=headers)
        res = conn.getresponse()
        data = res.read()


        print("Status: {}".format(res.status))
        if res.status == 404:
            print("no have mac {}".format(self.mac))
        elif res.status == 204:
            print('delete mac {}'.format(self.mac))
        else:
            print("Exception!!")

    def __str__(self) :
        return f"{self.mac}"

