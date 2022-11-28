from configparser import ConfigParser
from os import popen

config = ConfigParser()
config.read('config.ini')

devMode = config.getboolean('installation', 'devInstallation')
conda = config.getboolean('installation', 'useConda')

packages = "pillow pandas"

if devMode == True:
    packages = packages + " tensorflow keras opencv"

if conda == True:
    packageManager = 'conda'
else:
    packageManager = 'pip'

popen(packageManager + " " + packages)