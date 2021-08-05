#
# documentation:
import requests
import json
import urllib3

# Return codes expected by Nagios
OK = 0
WARNING = 1
CRITICAL = 2
UNKNOWN = 3

#Disable warnings https
urllib3.disable_warnings()

class AzureAppHealthChecks:
    def __init__(self, url):
        
        #initial
        self.url = url
               

    def get_status_data(self):
            
        #Add tags to the URL
        url = self.url
        
        # requests doc http://docs.python-requests.org/en/v0.10.7/user/quickstart/#custom-headers
        r = requests.get(url=url, verify=False)
        
        return r.json(), r.status_code
    
    def check_status_data(self):

        #Vars
        retrcode = OK
		
        #Create tuple with json and status code
        azure_health_status = self.get_status_data()
        
        msgdata = ''
        msgerror = '{:>10}'.format(azure_health_status[0]['entries']['smartAccess_health_check']['description'])
        retrperfdata = ''
        retrmsg = ''
        import pdb; pdb.set_trace()
        #Validate Data
        if azure_health_status[0]['status'] != 'Healthy':
            retrcode = CRITICAL

        msgerror += msgdata
         
        return retrcode, msgerror
        