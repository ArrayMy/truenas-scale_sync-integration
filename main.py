#Attr --target (string) --destination (string) --time (array)
from array import array
from ast import arg
from asyncio import constants
from asyncio.windows_events import NULL
from hashlib import new
import os
import string

class OSClass():
    CacheIndex = 1
    CacheData = []
    #construct
    def __init__(self, *args):
        self._target = args[0]
        self._destination = args[1]
        self._time = args[2]
        del(args)    
    #every call
    def __call__(self, Msg:string): # String = encoded decoded base64
        print(Msg)
        print("Debuging {} mode".format(Msg))     
    #define operation with instance
    def __add__(self, Msg:string): # String = encoded decoded base64
        return self.CacheData.append(Msg)
    #loading dat in cache      
    def LoadInformation(self, input:string): # String = encoded decoded base64
        _output = input
        self.Cache(_output)
        del(_output)     
    #cache loop     
    def Cache(self, _data:dict):
        if(len(self.CacheData)>self.CacheIndex):
            self.CacheData.insert(0,_data)
            self.CacheData.pop(2)
        else:
            self.CacheData.extend(_data)           
    #geting data for load in cache    
    def getFilesInFolder(self, dir:string):
        _files = os.scandir(dir)
        for _file in _files:
            if not _file.name.startswith('.'):  #files starting with . need permissions
                if _file.is_file():
                    #format(_file.name) FILENAME (feed)
                    #format(self.getBytableValue(_file.stat().st_size),'.2g')  FILESIZE (feed)
                    pass
                else:
                    print("FOLDER: {}".format(_file.name))
    #inputs for convert methods is byte   TODO:Convert class             
    def KiloBytes(self, _input:int):
        return _input/8000
    def MegaBytes(self, _input:int):
        return _input/80000
    def KiloBites(self, _input:int):
        return _input/1000
    def MegaBites(self, _input:int):
        return _input/10000
    def getBytableValue(self, _input:int):
        if(_input > 1000):
            _input = self.KiloBites(_input)
            unit = 'Kb'
            if(_input > 1000):
                _input = self.MegaBites(_input)
                unit = 'Mb'
        else:
            unit = 'b' 
        if(unit != 'b'):
            _input = format(_input, '.2g')
        return{_input, unit}  
Target = OSClass(".",".","3")
#Destination = OSClass(".",".","30")
Target.LoadInformation('A0')
Target.LoadInformation('A1')
Target.LoadInformation('A2')
# Target.LoadInformation('A3')
# Target.LoadInformation('A4')
# Target.LoadInformation('A5')
# Target.getFilesInFolder('..')
#Target("505")
#print(Target+"WAU!")
#Target.test()