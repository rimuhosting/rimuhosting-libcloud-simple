import sys
# libcloud.provider contains the neccessary functions to get the driver
# implementation
from libcloud.providers import *

# Get the RimuHostingNodeDriver class
rimu_driver = get_driver(Provider.RIMUHOSTING)

# Create an instance of RimuHostingNodeDriver.
# Grab the api_key from argv[1]
rh = rimu_driver(sys.argv[1])
sizes = rh.list_sizes()

for size in sizes:
    print "Plan ID: %s, RAM: %smb, Disk: %sgb, Bandwidth: %sgb, Price: USD%s" %(size.id, size.ram,size.disk, size.bandwidth, size.price)

