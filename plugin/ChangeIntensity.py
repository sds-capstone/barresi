#
#
#
#    <CustomTools>
#      <Menu>
#       <Item name="Change Intensity" icon="Python3">
#         <Command>Python3XT::changeIntensity(%i)</Command>
#       </Item>
#      </Menu>
#    </CustomTools>
#     

#  Description:
#  This XTension change the intensity above a user-defined threshold
#  to a user-defined highest level and any intensity below the threshold
#  to zero.


import ImarisLib

# GUI imports
from tkinter import *
from tkinter import messagebox

def changeIntensity(aImarisId):
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
    global Entry1, Entry2
    ###########################################################################
    def dialog():
        global Entry1, vThreshold, Entry2, vNewHigh
        vThreshold=Entry1.get()
        vThreshold=float(vThreshold)
        vNewHigh=Entry2.get()
        vNewHigh=float(vNewHigh)
        root.destroy()
    
    root=Tk()
    root.geometry("218x75-0+0")
    #Set input as the top level window
    root.attributes("-topmost", True)
    ##################################################################
    #Set input in center on screen
    # Gets the requested values of the height and width.
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    # Gets both half the screen width/height and window width/height
    positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
    # Positions the window in the center of the page.
    root.geometry("+{}+{}".format(positionRight, positionDown))
    ##################################################################
    
    Label(root,text="Targeted Intensity Level:").grid(row=0) ##grid sets the location
    Entry1=Entry(root,justify='center',width=10)
    Entry1.grid(row=0, column=1)
    Entry1.insert(0, 100) # set default entry as 100

    Label(root,text="Intended Intensity Level:").grid(row=1)
    Entry2=Entry(root,justify='center',width=10)
    Entry2.grid(row=1, column=1)
    Entry2.insert(0, 100) 
    
    # Creates Button
    Single=Button(root, text="Change Intensity", bg='blue', fg='white',command=dialog) # Previously defined dialog is called here
    # Set button location
    Single.grid(row=1, column=1)
    # Call the input window for display
    mainloop()

    ############################################################################
    ############################################################################
    
    
    ## Get the Dataset
    vImage = vImarisApplication.GetImage(0)

    # Set the Channel Index to the first one
    vChannelIndex=0
    # Set the new lowest intensity as 0
    vNewValueLow=0
    
    # Change the Intensity
    vImarisApplication.GetImageProcessing().ThresholdBothChannel(vImage,vChannelIndex,vThreshold,vNewValueLow,vNewHigh)

    


    
