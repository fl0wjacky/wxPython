#! /usr/bin/env python3 
# coding:utf-8

import os
import sys

'''对os.walk()的认识，其定义的函数会自动应用在子路径上'''

def searchPath(path,name,sep):
    for dirpath,dirnames,filenames in os.walk(path):
        for file in filenames:
            if file == name:
                print(sep + os.path.join(dirpath,file))
        #sep += '  '

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('please enter like this:./search.py thePath theFullnameOfTheFile')
    else:
        #print(sys.argv)
        searchPath(sys.argv[1],sys.argv[2],' ')
