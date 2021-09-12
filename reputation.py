import sys
import shodan
from termcolor import colored

# Insert your own API keys here:
SHODAN_API_KEY = "YOUR_API_KEY"

# Shodan IP check
def shodan_check(ip):
    api = shodan.Shodan(SHODAN_API_KEY)
    
    # Lookup the host
    host = api.host(ip)

    # Print general info
    print(colored("""
  ___ _            _           
 / __| |_  ___  __| |__ _ _ _  
 \__ \ ' \/ _ \/ _` / _` | ' \ 
 |___/_||_\___/\__,_\__,_|_||_|


IP: {}
Organization: {}
Operating System: {}

    """, "red").format(host["ip_str"], host.get("org", "n/a"), host.get("os", "n/a")))

    # Print all banners
    for item in host["data"]:
        print(colored("""
Port: {}
Banner: {}
        """, "red").format(item["port"], item["data"]))


# Check input is in the correct format
if len(sys.argv) != 2:
    print("Usage: %s <IP>" % sys.argv[0])
    sys.exit(1)

if SHODAN_API_KEY != "YOUR_API_KEY" and SHODAN_API_KEY != "":
    shodan_check(sys.argv[1])

