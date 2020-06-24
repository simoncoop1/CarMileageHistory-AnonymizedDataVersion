import os
import sys
import zipfile
import gzip
import shutil




## latest as of jun - 2020
## this is a script to extract the data

files = ['test_result_2008.txt.gz',  'test_result_2014.txt.gz',
'dft_test_result_2018.zip',  'test_result_2009.txt.gz',  'test_result_2015.txt.gz',
'dft_test_result_2019.zip',  'test_result_2010.txt.gz',  'test_result_2016.txt.gz',
'test_result_2005.txt.gz',   'test_result_2011.txt.gz',  'test_result_2017.zip',
'test_result_2006.txt.gz',   'test_result_2012.txt.gz', 'test_result_2007.txt.gz',
'test_result_2013.txt.gz']

#check files are present
allpresent = True
for f in files:
        if (os.path.exists(f) == False) | (os.path.isfile(f) == False):
            allpresent = False
            print (f + " not found")

if allpresent == False:
    print("some files not found. exiting")
    sys.exit()


for f in files:
    print("extracting. " + f)    
    if f.endswith("txt.gz"):
        with gzip.open(f, 'rb') as f_in:
            with open(f[:-3], 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
    elif f.endswith("zip"):     
        with zipfile.ZipFile(f, 'r') as zip_ref:            
            zip_ref.extractall('.')
