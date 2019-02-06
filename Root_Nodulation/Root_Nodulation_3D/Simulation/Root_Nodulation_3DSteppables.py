
from PySteppables import *
import CompuCell
import time
import sys

from PySteppablesExamples import MitosisSteppableBase


class ConstraintInitializerSteppable(SteppableBasePy):
    def __init__(self,_simulator,_frequency=1):
        SteppableBasePy.__init__(self,_simulator,_frequency)
    def start(self):
        for cell in self.cellList:
            cell.targetVolume=125
            cell.lambdaVolume=2.0

class Root_Nodulation_3DSteppable(SteppableBasePy):    

    def __init__(self,_simulator,_frequency=1):
        SteppableBasePy.__init__(self,_simulator,_frequency)
    def start(self):
        # any code in the start function runs before MCS=0
        pass
    def step(self,mcs):        
        #type here the code that will run every _frequency MCS
        for cell in self.cellList:
            print "cell.id=",cell.id
    def finish(self):
        # Finish Function gets called after the last MCS
        pass

class Switch(SteppableBasePy):
    def __init__(self,_simulator,_frequency=1):
        SteppableBasePy.__init__(self,_simulator,_frequency)
    def step(self,mcs):
        for cell in self.cellList:
            if cell.type == 2:
               for neighbor, commonSurfaceArea in self.getCellNeighborDataList(cell):
                   if neighbor:
                       if neighbor.type==4 and mcs%25==0 and mcs>1:
                        cell.type = 5
                        
class ElongationFlexSteppable(SteppableBasePy):
    def __init__(self,_simulator,_frequency=10):
        SteppableBasePy.__init__(self, _simulator, _frequency)
        # self.lengthConstraintPlugin=CompuCell.getLengthConstraintPlugin()
        
        
    def start(self):
        pass

    def step(self,mcs):
        for cell in self.cellList:
            if cell.type==4: 
                self.lengthConstraintPlugin.setLengthConstraintData(cell,20,20) # cell , lambdaLength, targetLength
                self.connectivityGlobalPlugin.setConnectivityStrength(cell,10000000) #cell, strength

class MitosisSteppable(MitosisSteppableBase):
    def __init__(self,_simulator,_frequency=1):
        MitosisSteppableBase.__init__(self,_simulator, _frequency)
    
    def step(self,mcs):
        # print "INSIDE MITOSIS STEPPABLE"
        cells_to_divide=[]
        for cell in self.cellList:
            if cell.type==5 and mcs%250==0:
                
                cells_to_divide.append(cell)
                
        for cell in cells_to_divide:
            # to change mitosis mode leave one of the below lines uncommented
            #self.divideCellRandomOrientation(cell)
            # self.divideCellOrientationVectorBased(cell,1,0,0)                 # this is a valid option
             self.divideCellAlongMajorAxis(cell)                               # this is a valid option
            # self.divideCellAlongMinorAxis(cell)                               # this is a valid option

    def updateAttributes(self):
        #self.parentCell.targetVolume /= 2.0 # reducing parent target volume                 
        self.cloneParent2Child()            
        
        # for more control of what gets copied from parent to child use cloneAttributes function
        # self.cloneAttributes(sourceCell=self.parentCell, targetCell=self.childCell, no_clone_key_dict_list = [attrib1, attrib2] )
        
        
        if self.parentCell.type==5:
            self.childCell.type=5
        #else:
            #self.childCell.type=1         