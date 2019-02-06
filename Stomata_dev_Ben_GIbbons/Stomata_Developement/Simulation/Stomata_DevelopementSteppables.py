
from PySteppables import *
import CompuCell
import sys

from PySteppablesExamples import MitosisSteppableBase
            

class ConstraintInitializerSteppable(SteppableBasePy):
    def __init__(self,_simulator,_frequency=1):
        SteppableBasePy.__init__(self,_simulator,_frequency)
    def start(self):
        for cell in self.cellList:
            if cell.type != 3:
                cell.targetVolume=25
                cell.lambdaVolume=2.0
            else:
                cell.targetVolume=10
                cell.lambdaVolume=2.0
                
        
        

class Switch(SteppableBasePy):
    def __init__(self,_simulator,_frequency=1):
        SteppableBasePy.__init__(self,_simulator,_frequency)
    def step(self,mcs):
        for cell in self.cellList:
            if cell.type == 3: #meristemoid 'conflict' resolves in commiting to pavement cell lineage
               for neighbor, commonSurfaceArea in self.getCellNeighborDataList(cell):
                   if neighbor:
                       if neighbor.type==3 or neighbor.type==5 or neighbor.type==6:
                        cell.type = 4 #7
                       elif mcs > 250:
                           cell.type = 5
            elif cell.type == 4: #spacing SLGC if there is no stomata lineage revert to MMC
                i = 0;
                for neighbor, commonSurfaceArea in self.getCellNeighborDataList(cell):
                    if neighbor:
                       if neighbor.type==3 or neighbor.type==5 or neighbor.type==6:
                           i=1
                           if neighbor.type == 5:
                                cell.type = 7
                if i == 0 and mcs%50 == 0:
                    cell.type = 2
                
                    
            elif cell.type == 1: #spacing protoderm if there is no stomata lineage revert to MMC EPFL-ERL regulated
                i = 0;
                for neighbor, commonSurfaceArea in self.getCellNeighborDataList(cell):
                    if neighbor:
                       if neighbor.type==3 or neighbor.type==5 or neighbor.type==6:
                           i=1
                if i == 0:
                    cell.type = 2
                elif mcs > 250:
                    cell.type = 7
             #elif cell.type == 2 and mcs > 250:
               #cell.type = 4 
            
         
                
                    
                
                


class GrowthSteppable(SteppableBasePy):
    def __init__(self,_simulator,_frequency=1):
        SteppableBasePy.__init__(self,_simulator,_frequency)
    def step(self,mcs):
        for cell in self.cellList:
            cell.targetVolume+=1        
    # alternatively if you want to make growth a function of chemical concentration uncomment lines below and comment lines above        
        # field=CompuCell.getConcentrationField(self.simulator,"PUT_NAME_OF_CHEMICAL_FIELD_HERE")
        # pt=CompuCell.Point3D()
        # for cell in self.cellList:
            # pt.x=int(cell.xCOM)
            # pt.y=int(cell.yCOM)
            # pt.z=int(cell.zCOM)
            # concentrationAtCOM=field.get(pt)
            # cell.targetVolume+=0.01*concentrationAtCOM  # you can use here any fcn of concentrationAtCOM  
        
       
       

                        
class MitosisSteppable(MitosisSteppableBase):
    def __init__(self,_simulator,_frequency=1):
        MitosisSteppableBase.__init__(self,_simulator, _frequency)
    
    def step(self,mcs):
        # print "INSIDE MITOSIS STEPPABLE"
        cells_to_divide=[]
        for cell in self.cellList:
            if cell.type==2:
                #if mcs%50==0:
                cells_to_divide.append(cell)
            #elif cell.type==3:#Amplifying
                #for neighbor, commonSurfaceArea in self.getCellNeighborDataList(cell):
                   #if neighbor:
                        #if neighbor.type==0:
                            #cells_to_divide.append(cell)
            elif cell.type == 5 and mcs > 275:
                cells_to_divide.append(cell)
        for cell in cells_to_divide:
            # to change mitosis mode leave one of the below lines uncommented
            # self.divideCellRandomOrientation(cell)
             self.divideCellOrientationVectorBased(cell,0,1,0)                 # this is a valid option
            # self.divideCellAlongMajorAxis(cell)                               # this is a valid option
            # self.divideCellAlongMinorAxis(cell)                               # this is a valid option

    def updateAttributes(self):
        self.parentCell.targetVolume /= 1.3333333333 # reducing parent target volume                 
        self.cloneParent2Child()            
        
        # for more control of what gets copied from parent to child use cloneAttributes function
        # self.cloneAttributes(sourceCell=self.parentCell, targetCell=self.childCell, no_clone_key_dict_list = [attrib1, attrib2] )
        
        
        if self.parentCell.type==2:
            self.childCell.type=3
            self.parentCell.type=4
        #elif self.parentCell.type==3:
            #self.childCell.type=7
        elif self.parentCell.type==5:
            self.parentCell.targetVolume /=2.0 # reducing parent target volume                 
            self.cloneParent2Child()
            self.childCell.type=6
            self.parentCell.type=6
            
        
        