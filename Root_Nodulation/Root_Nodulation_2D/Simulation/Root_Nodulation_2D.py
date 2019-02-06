
import sys
from os import environ
from os import getcwd
import string

sys.path.append(environ["PYTHON_MODULE_PATH"])


import CompuCellSetup


sim,simthread = CompuCellSetup.getCoreSimulationObjects()
            
# add extra attributes here
            
CompuCellSetup.initializeSimulationObjects(sim,simthread)
# Definitions of additional Python-managed fields go here
        
#Add Python steppables here
steppableRegistry=CompuCellSetup.getSteppableRegistry()
        
from Root_Nodulation_2DSteppables import Root_Nodulation_2DSteppable
steppableInstance=Root_Nodulation_2DSteppable(sim,_frequency=1)
steppableRegistry.registerSteppable(steppableInstance)

from Root_Nodulation_2DSteppables import Switch
SwitchInstance=Switch(sim,_frequency=1)
steppableRegistry.registerSteppable(SwitchInstance)
        
from Root_Nodulation_2DSteppables import ElongationFlexSteppable
elongationFlexSteppable=ElongationFlexSteppable(_simulator=sim,_frequency=50)
steppableRegistry.registerSteppable(elongationFlexSteppable)

from Root_Nodulation_2DSteppables import MitosisSteppable
MitosisSteppableInstance=MitosisSteppable(sim,_frequency=1)
steppableRegistry.registerSteppable(MitosisSteppableInstance)

from Root_Nodulation_2DSteppables import ConstraintInitializerSteppable
ConstraintInitializerSteppableInstance=ConstraintInitializerSteppable(sim,_frequency=1)
steppableRegistry.registerSteppable(ConstraintInitializerSteppableInstance)        
CompuCellSetup.mainLoop(sim,simthread,steppableRegistry)
        
        