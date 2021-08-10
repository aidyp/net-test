import subprocess
import sys

def test_connection(domain, host):
    '''
    Tests to see whether this host can connect to your webserver 
    '''
    
    passed = True 
    test_string = b'<h1>Hello World</h1>\n'
    cmd = 'curl ' + web_domain + ' --connect-timeout 5'
    p = subprocess.Popen("ssh -i {keyname} {user}@{host} {cmd}".format(keyname='public-box.pem', user='ec2-user', host=host, cmd=cmd), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if p.stdout.readline() == test_string:
        print("This instance can connect!")
        passed = False
    else:
        print("This instance can't connect!")
    print("Passed: ", passed)
    
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python3 main.py <web_domain> <instance_url>')
    
    web_domain = sys.argv[1]
    host = sys.argv[2]
    
    test_connection(web_domain, host)