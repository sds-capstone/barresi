#
#
#
#    <CustomTools>
#      <Menu>
#       <Item name="Count Number of Surfaces" icon="Python3">
#         <Command>Python3XT::surfaceCount(%i)</Command>
#       </Item>
#      </Menu>
#    </CustomTools>

#  Description:
#  This XTension will copy the filament in the specified time point and
#  copy it to selected Destination timepoint.  All spines and dendrites
#  will be copied.   Default options will take filaments in current visible
#  timepoint to the next timepoint.

#  This process will NOT overwrite any existing filaments that may be in
#  the Destination timepoint.
#
#There is also and option to copy Filaments from a specific timepoint to all
#timepoints.   Note:  This will NOT duplicate filament in original timepoint.


import ImarisLib

# GUI imports
from tkinter import *
from tkinter import messagebox
from pandas import DataFrame

def surfaceCount(aImarisId):
    # Create an ImarisLib object
    vImarisLib = ImarisLib.ImarisLib()
    # Get an imaris object with id aImarisId
    vImarisApplication = vImarisLib.GetApplication(aImarisId)
    # Get the factory
    vFactory = vImarisApplication.GetFactory()
    # Get the currently loaded dataset
    vImage = vImarisApplication.GetDataSet()
    # Get the Surpass scene
    vSurpassScene = vImarisApplication.GetSurpassScene()
    
  
    vSelected = vImarisApplication.GetSurpassSelection()
    
    vSurfaces = vFactory.ToSurfaces(vSelected)
    vNumberOfSurfaces = vSurfaces.GetNumberOfSurfaces()


    vText = 'Number of Surfaces: ' + str(vNumberOfSurfaces)

    #__msgbox(vText)

    #df = DataFrame({'Point': 1, 'Farthest Distance': vFarthestDistance})
   # df.to_excel('test.xslx', sheet_name= 'sheet1', index = False)
    f = open(r'C:\Users\zfishlab\Documents\GitHub\barresi\Results\CellCount.txt', 'w')
    f.write(vText)
    f.close()