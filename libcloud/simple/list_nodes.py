import sys
# libcloud.provider contains the neccessary functions to get the driver
# implementation
from libcloud.providers import *

# Get the RimuHostingNodeDriver class
rimu_driver = get_driver(Provider.RIMUHOSTING)

# Create an instance of RimuHostingNodeDriver.
# Grab the api_key from argv[1]
rh = rimu_driver(sys.argv[1])
nodes = rh.list_nodes()

for node in nodes:
    print "Node ID: %s, Name: %s, IPs: %s, State: %s" %(node.id, node.name,node.public_ip, node.state)

