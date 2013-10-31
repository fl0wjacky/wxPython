#! /usr/bin/env python 
# coding:utf-8

import os
import sys

def searchPath(path,name):
    for dirpath,dirnames,filenames in os.walk(path):
        for file in filenames:
            if file == name:
                print(dirpath,file)
        for dirname in dirnames:
            subpath = os.path.join(dirpath,dirname)
            searchPath(subpath,name)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('please enter like this:./search thePath thePartOfFilename')
    else:
        print(sys.argv)
        searchPath(sys.argv[1],sys.argv[2])
