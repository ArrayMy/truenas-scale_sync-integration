#Attr --target (string) --destination (string) --time (array)
from array import array
from ast import arg
from asyncio.windows_events import NULL
from hashlib import new
import os
import string

class OSClass():
    CacheIndex = 1 #Maximum 2 -> OSClass.Cache()
    Cache = ["", ""]
    def __init__(self, *args):
        self._target = args[0]
        self._destination = args[1]
        self._time = args[2]
        del(args)
        
    def LoadInformation(self):
        _output = ["A"]
        self.Cache(_output)
        del(_output)
        
    def Cache(self, _data:dict):
        if(len(self.Cache)):
            print("true")
        if(len(self.Cache)>self.CacheIndex):
            self.Cache.insert(_data,0)
            self.Cache.pop(2)
        else: # 2x Init else, _data1, _data2
            self.Cache.extend(_data)        
        print(self.Cache)
            
Target = OSClass(".",".","3")
Target.LoadInformation()
Destination = OSClass(".",".","30")

Target.LoadInformation()

def getFilesInFolder(dir:string):
        pass