import requests
import sys


def launch_nasty_attack(domain):
    '''
    A hacker has figured out a vulnerability in our web application. 
    They are adding a custom header that gives them admin access
    '''
    
    custom_headers = {'X-Sneaky-Hack': 'pwned'}
    try:
        r = requests.get(domain, headers=custom_headers)
        print("The hacker can connect!")
        return r.status_code
    except requests.exceptions.RequestException as e:
        print("Hacker can't connect -- nice!")
        return 0

def regular_customer(domain):
    '''
    Regular customers connect normally. We don't want to stop them connecting 
    '''
    try:
        r = requests.get(domain)
        return r.status_code
    except requests.exceptions.RequestException as e: 
        print("Customers can't connect to your webserver: ", str(e))
        return 0 
    

def evaluate_scenario(domain):
    '''
    Check whether the firewall rule is dropping the right packets 
    '''
    
    passed = True 
    
    if regular_customer(domain) != 200 or launch_nasty_attack(domain) == 200:
        passed = False 
        
        
    print("Passed: ", passed)
        
    
    
    



if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <Your Web Domain>")
        sys.exit(0)
    
    target_server = sys.argv[1] 
    evaluate_scenario(target_server)