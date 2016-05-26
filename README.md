# ganglia_python_modules

The ganglia python modules are extended modules for use with Ganglia Cluster Monitoring Tool. 

##Modules
readcache.py allows you to keep track of the cache size of your scidb cluster. 
Make sure that the ganglia user has rx access to the cache folder in order to get a correct reading. 

##Generic python module install instructions

Add the *.conf file to your ganglia conf folder /etc/ganglia/conf.d/

sudo cp cacheread.conf /etc/ganglia/conf.d/
 
Add the *.py file to /usr/lib64/ganglia/python_modules/

sudo cp cacheread.py /usr/lib64/ganglia/python_modules/

Then restart gmond. 
sudo service gmond restart
