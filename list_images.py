import sys
# libcloud.provider contains the neccessary functions to get the driver
# implementation
from libcloud.providers import *

# Get the RimuHostingNodeDriver class
rimu_driver = get_driver(Provider.RIMUHOSTING)

# Create an instance of RimuHostingNodeDriver.
# Grab the api_key from argv[1]
rh = rimu_driver(sys.argv[1])
images = rh.list_images()

for image in images:
    print "Image ID: %s \t\t Description: %s" %(image.id, image.name)

