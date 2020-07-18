#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import subprocess
from glob import glob
import re
def main():
    l=sorted(list(glob('20*.html')))
    for f in l:
        if re.search('2018-04-01|2018-05-01',f):continue
        cmd='cp {} sankatu.html'.format(f)
        subprocess.run(cmd,shell=True,check=True)
        print(cmd)
        cmd='git commit -m "{}" .'.format(f)
        subprocess.run(cmd,shell=True,check=True)
        print(cmd)
if __name__=='__main__':main()

    
    
