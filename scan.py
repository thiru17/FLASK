import schedule
import time
from subprocess import Popen,PIPE
import os


def func():
	 a= Popen(
        ['rustscan',' -a',' 76.223.65.111',' -r',' 1-65535'] , shell=True ,stdout= PIPE,stderr= PIPE ,universal_newlines=True)
     out,err=a.communicate()
     return out  


