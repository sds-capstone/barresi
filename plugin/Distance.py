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
    global Entry1#, aCopyAll
    ###########################################################################
    #aCopyAll=False
    def dialog():
        global Entry1, vNewIntensity#, aCopyAll
        vNewIntensity=Entry1.get()
        vNewIntensity=float(vNewIntensity)
        #aCopyAll=False
        root.destroy()

    def __msgbox(aText):
        vTk = Tk()
        vTk.wm_title("XTDisplayImarisId")
        vWidget = Label(vTk, text = aText, justify = 'left', padx = 10, pady = 10)
        vWidget.pack()
        vTk.mainloop()
    
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
    
    Label(root,text="Intensity Level:").grid(row=0)
    Entry1=Entry(root,justify='center',width=10)
    Entry1.grid(row=0, column=1)
    Entry1.insert(0, 100) ##ask Shay about what to set default as!!
    
    Single=Button(root, text="Selected Spot", bg='blue', fg='white',command=dialog)
   # Alltime=Button(root, text="All Surfaces",bg='red', command=All)
    Single.grid(row=2, column=1)
    #Alltime.grid(row=2, column=0)
    
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
    vSelected = vImarisApplication.GetSurpassSelection()
    #vSpots = vFactory.ToSpots(vSelected)
    
   # vSelectedSpots = vSpots.GetSelectedIndices()
    

    #aPositionsXYZ = vSpots.GetPositionsXYZ()
    vImage = vImarisApplication.GetImage(0)
    #vDataSetOut=vImarisApplication.GetImageProcessing().DistanceTransformDataSet(vSelected,vNewIntensity,False)
    #vNumberOfImages = vImarisApplication.GetNumberOfImages()

    vFarthestDistance = 0

    """ for i in range(0, len(vDataSetOut)):
        if vDataSetOut[i] > vFarthestDistance :
            vFarthestDistance = vDataSetOut[i]
     """
    vText = 'Farthest Distance: ' + str(vSelected)

    #__msgbox(vText)

    #df = DataFrame({'Point': 1, 'Farthest Distance': vFarthestDistance})
   # df.to_excel('test.xslx', sheet_name= 'sheet1', index = False)
    f = open(r'C:\Users\zfishlab\Downloads\test.txt', 'w')
    f.write(vText)
    f.close()
    


    