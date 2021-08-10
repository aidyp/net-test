import requests
import sys


def launch_nasty_attack(domain):
    '''
    A hacker has figured out a vulnerability in our web application. 
    They are adding a custom header that gives them admin access
    '''
    
    custom_headers = {'X-Sneaky-Hack': 'pwned'}
    try:
        r = requests.get(domain, headers=custom_headers, timeout = 5)
        print("The hacker can connect!")
        return False
    except requests.exceptions.RequestException as e:
        print("Hacker can't connect -- nice!")
        return True

def regular_customer(domain):
    '''
    Regular customers connect normally. We don't want to stop them connecting 
    '''
    try:
        r = requests.get(domain, timeout = 5)
        return True
    except requests.exceptions.RequestException as e: 
        print("Customers can't connect to your webserver: ", str(e))
        return False
    

def evaluate_scenario(domain):
    '''
    Check whether the firewall rule is dropping the right packets 
    '''
    
    passed = regular_customer(domain) and launch_nasty_attack(domain)
    print("Passed: ", passed)
        
    
    
    



if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <Your Web Domain>")
        sys.exit(0)
    
    target_server = sys.argv[1] 
    evaluate_scenario(target_server)