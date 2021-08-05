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

class WebAppHealthChecks:
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
        webapp_health_status = self.get_status_data()        
                           
        msgdata = ''
        msgerror = '{:>10}'.format(webapp_health_status.get('entries').get('process_health_check').get('description', ''))           
        retrperfdata = ''
        retrmsg = ''
        
        #Validate Data
        if webapp_health_status[0]['status'] != 'Healthy':
            retrcode = CRITICAL

        msgerror += msgdata
         
        return retrcode, msgerror
        