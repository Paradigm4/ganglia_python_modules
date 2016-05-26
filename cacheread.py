'''
Created on May 26, 2016

@author: Jonathan Rivers
'''
import os, sys
from os.path import join,getsize
import pwd
import re

def print_names(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path,followlinks=True):
        for d in dirnames:
            if(re.match(r'tmp', d)):
                itempath = os.path.join(dirpath, d)
                #print itempath
                total_size += os.path.getsize(itempath)
    #print total_size            
    return total_size



scidb_folder = "/home/scidb/scidb_data15_12"

def readcache_handler(name):  
    
    try:
        rtnval = print_names(scidb_folder)
    
    except IOError:
        return 0

    return rtnval

def metric_init(params):
    global descriptors, acpi_file

    if 'scidb_folder' in params:
        scidb_folder = params['scidb_folder']

    d1 = {'name': 'readcache',
        'call_back': readcache_handler,
        'time_max': 90,
        'value_type': 'float',
        'units': 'bytes',
        'slope': 'both',
        'format': '%u',
        'description': 'Size of the SciDB temp folder',
        'groups': 'health'}

    descriptors = [d1]

    return descriptors

def metric_cleanup():
    '''Clean up the metric module.'''
    pass

#This code is for debugging and unit testing
if __name__ == '__main__':
    metric_init({})
    for d in descriptors:
        v = d['call_back'](d['name'])
        print 'value for %s is %u' % (d['name'],  v)
        
        
        
        
