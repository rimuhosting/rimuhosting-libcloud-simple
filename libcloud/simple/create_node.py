import sys
# libcloud.provider contains the neccessary functions to get the driver
# implementation
from libcloud.providers import *

def usage():
    print sys.argv[0], "<apikey> <node FQDN> <node image> <node size>"
    sys.exit(1)    

if len(sys.argv) != 5:
    usage()

# Get the RimuHostingNodeDriver class
rimu_driver = get_driver(Provider.RIMUHOSTING)

# Create an instance of RimuHostingNodeDriver.
# Grab the api_key from argv[1]
rh = rimu_driver(sys.argv[1])
sizes = rh.list_sizes()
images = rh.list_images()

try:
    size = filter(lambda x : x.id == sys.argv[4],sizes)[0]
except:
    print "No size found matching '%s'" % (sys.argv[4])
    usage()

try:
    image = filter(lambda x : x.id == sys.argv[3],images)[0]
except:
    print "No image found matching '%s'" % (sys.argv[3])
    usage()

node = rh.create_node(sys.argv[2], image, size)

print "ID: %s, Name: %s, Public IPs: %s, State: %s, Password: %s" % (node.id, node.name,node.public_ip,
                                            node.state, node.extra['password'])
