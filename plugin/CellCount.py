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

def surfaceCount(aImarisId):
    # Create an ImarisLib object
    vImarisLib = ImarisLib.ImarisLib()
    # Get an imaris object with id aImarisId
    vImarisApplication = vImarisLib.GetApplication(aImarisId)
    # Get the factory
    vFactory = vImarisApplication.GetFactory()
  
    #Get the Selected Objects
    vSelected = vImarisApplication.GetSurpassSelection()
    
    #Get the Surface objects
    vSurfaces = vFactory.ToSurfaces(vSelected)
    
    #Get the number of surfaces
    vNumberOfSurfaces = vSurfaces.GetNumberOfSurfaces()

    #Stringify the number and add to text
    vText = 'Number of Surfaces: ' + str(vNumberOfSurfaces)
    
    #Write it out into text file
    f = open(r'C:\Users\zfishlab\Documents\GitHub\barresi\Results\CellCount.txt', 'w') #Specifify the rout
    f.write(vText)
    f.close()
