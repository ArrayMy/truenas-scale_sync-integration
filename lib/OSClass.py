#Attr --target (string) --destination (string) --time (array)
from array import array
from ast import arg
import os #TODO: SECURE WITH FROM
import string #TODO: SECURE WITH FROM
import time #TODO: SECURE WITH FROM
import stat #TODO: SECURE WITH FROM

class OSClass(): #TODO: Add polymorf from os
    CacheIndex = 1
    CacheData = []
    def __init__(self, *args):
        self._target = args[0]
        self._destination = args[1]
        self._time = args[2]
        del(args)   
    def __call__(self, Msg:string): 
        print("Debuging mode: {}".format(Msg))     
    def __add__(self, Msg:string):
        return self.CacheData.append(Msg)  
    def LoadInformation(self, input:string):
        _output = input
        self.Cache(_output)
        del(_output)       
    def Cache(self, _data:dict):
        if(len(self.CacheData)>self.CacheIndex):
            self.CacheData.insert(0,_data)
            self.CacheData.pop(2)
        else:
            self.CacheData.extend(_data)           
    def getFilesInFolder(self, dir:string):
        _files = os.scandir(dir)
        for _file in _files:
            if not _file.name.startswith('.'):
                if _file.is_file():
                    #format(_file.name) FILENAME (feed)
                    #format(self.getBytableValue(_file.stat().st_size),'.2g')  FILESIZE (feed)
                    pass
                else:
                    #print("FOLDER: {}".format(_file.name))
                    pass
    def getFileLastModifiedTime(self, dir:string):
        _Obj= os.stat(dir)
        _time = time.ctime(_Obj [stat.ST_MTIME] )
        return(_time)
    #TODO:Convert class             
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
            unit = 'Kb' #TODO: Without units in class!
            if(_input > 1000):
                _input = self.MegaBites(_input)
                unit = 'Mb' #TODO: Without units in class!
        else:
            unit = 'b'  #TODO: Without units in class!
        if(unit != 'b'): #TODO: Without units in class! 
            _input = format(_input, '.2g') 
        return{_input, unit} 
    
    
    
#tmp
# Target = OSClass(".",".","3")
#Destination = OSClass(".",".","30")
# Target.LoadInformation('A0')
# Target.LoadInformation('A1')
# Target.LoadInformation('A2')
# Target.LoadInformation('A3')
# Target.LoadInformation('A4')
# Target.LoadInformation('A5')
# Target.getFilesInFolder('..')
#Target("505")
#print(Target+"WAU!")
#Target.test((
#Target.getFileLastModifiedTime("./index.php")#

