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

# Description:
#  This XTension gets the number of surfaces present and
#   outputs it into a text file.


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
    f = open(r'C:\Users\zfishlab\Documents\GitHub\barresi\Results\CellCount.txt', 'w') #Specifify the route and file name
    f.write(vText)
    f.close()
