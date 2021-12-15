#
#
#
#    <CustomTools>
#      <Menu>
#       <Item name="Farthest Distance from Spot" icon="Python3">
#         <Command>Python3XT::farthestDistance(%i)</Command>
#       </Item>
#      </Menu>
#      <SurpassTab>
#        <SurpassComponent name="bpFilaments">
#         <Item name="Farthest Distance from Spot" icon="Python3">
#           <Command>Python3XT::farthestDistance(%i)</Command>
#         </Item>
#        </SurpassComponent>
#      </SurpassTab>
#    </CustomTools>
# 
#
# Description:
#  This XTension will measure the distance from a spot to the farthest 
#  intensity of a user-defined level. Default levels are 100.
#
#


import ImarisLib
# GUI imports
from tkinter import *
from tkinter import messagebox
from pandas import DataFrame

def farthestDistance(aImarisId):
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
    global Entry1
    ###########################################################################
    #aCopyAll=False
    def dialog():
        global Entry1, vNewIntensity
        vNewIntensity=Entry1.get()
        vNewIntensity=float(vNewIntensity)
        #aCopyAll=False
        root.destroy()


    """ def All():
        global Entry1, vNewRadius, aCopyAll
        aCopyAll=True
        vNewRadius=Entry1.get()
        vNewRadius=float(vNewRadius)
        root.destroy()
     """
    root=Tk()
    root.geometry("200x50-0+0")
    #Set input as the top level window
    root.attributes("-topmost", True)
    ##################################################################
    #Set input in center on screen
    # Gets the requested values of the height and widht.
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    # Gets both half the screen width/height and window width/height
    positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
    # Positions the window in the center of the page.
    root.geometry("+{}+{}".format(positionRight, positionDown))
    ##################################################################
    
    Label(root,text="Intensity Level:").grid(row=0) ##grid sets the location
    Entry1=Entry(root,justify='center',width=10)
    Entry1.grid(row=0, column=1)
    Entry1.insert(0, 100) # set default entry as 100
    
    # Creates Button
    Single=Button(root, text="Selected Spot", bg='blue', fg='white',command=dialog) # Previously defined dialog is called here
   # Alltime=Button(root, text="All Surfaces",bg='red', command=All)
   # Set button location
    Single.grid(row=2, column=1)
    #Alltime.grid(row=2, column=0)
    
    # Call the input window for display
    mainloop()
    
    ############################################################################
    ############################################################################
    
     #Image properties
    vDataMin = (vImage.GetExtendMinX(),vImage.GetExtendMinY(),vImage.GetExtendMinZ())
    vDataMax = (vImage.GetExtendMaxX(),vImage.GetExtendMaxY(),vImage.GetExtendMaxZ())
    vDataSize = (vImage.GetSizeX(),vImage.GetSizeY(),vImage.GetSizeZ())
    vSizeT = vImage.GetSizeT()
    vSizeC = vImage.GetSizeC()
    aXvoxelSpacing= (vDataMax[0]-vDataMin[0])/vDataSize[0]
    aYvoxelSpacing= (vDataMax[1]-vDataMin[1])/vDataSize[1]
    aZvoxelSpacing = round((vDataMax[2]-vDataMin[2])/vDataSize[2],3)
    vSmoothingFactor=aXvoxelSpacing*2
    
    # Find the all objects
    vSelected = vImarisApplication.GetSurpassSelection()
    
    # Get the spot objects
    #vSpots = vFactory.ToSpots(vSelected)
    
    # Get the selected spots
    # vSelectedSpots = vSpots.GetSelectedIndices()
    
    # Find the position of the spot
    #aPositionsXYZ = vSpots.GetPositionsXYZ()
    
    # Get the data
    vImage = vImarisApplication.GetImage(0)
    
    # Find the array of all the distances to the spot
    #vDataSetOut=vImarisApplication.GetImageProcessing().DistanceTransformDataSet(vSelected,vNewIntensity,False)
   
    # Set the minimum distance for comparison 
    vFarthestDistance = 0
    
    # Find the largest distance
    """ for i in range(0, len(vDataSetOut)):
        if vDataSetOut[i] > vFarthestDistance :
            vFarthestDistance = vDataSetOut[i]
     """
    
    #Stringify the number and add to text
    vText = 'Farthest Distance: ' + str(vSelected)
    
    
    #df = DataFrame({'Point': 1, 'Farthest Distance': vFarthestDistance})
    # df.to_excel('test.xslx', sheet_name= 'sheet1', index = False)
    #Write it out into text file
    f = open(r'C:\Users\zfishlab\Documents\GitHub\barresi\Results\Distance.txt', 'w') #Specifify the route and file name
    f.write(vText)
    f.close()
