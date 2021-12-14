# Barresi Lab Capstone Group

Team Members:
- Summer Yu 
- Haley Schmidt
- Carol Milton
- Catherine Kung

# Installations Necessary for Python Plugins in Imaris
The following steps have already been implemented at the Imaris Workstation.

1. [Connect](https://www.urmc.rochester.edu/MediaLibraries/URMCMedia/multiphoton-core/documents/Imaris-XTension-User-Guide.pdf) plugin folder to the IMARIS python path

2. Find Path created for Xtension -> download Python 3.7.12 -> download VS Code in console command

3. Download Git for windows -> Download extension for Github

## Setting up Github extension for VS Code:

[guideline source](https://thenewstack.io/integrate-jupyter-notebooks-with-github/)

1. If there is an Error Message: not find “requests” -> Solve with pip install requests

2. Genereate ssh-keygen: id_rsa(file name), barresiprojectfall2021(key)

3. Add to ssh key in Github account and clone

4. git config --global user.name to enter username

5. git config --global user.email to enter email

6. [git clone](https://github.com/sat28/githubcommit)


# Documentation of Python XTensions for Imaris

## Linking to ImarisLib

Code to link to ImarisLib: 

    import ImarisLib

    def BLANK(aImarisId):

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


## Getting User Input and Displaying Output
Use the tkinter Python library to get input from the user and display output through the GUI (Graphical User Interface).

    global Entry1
    
    def dialog(): ## If you want to do so converting at the initial entry
        global Entry1, vChange
        vChanged=Entry1.get()
        vChange=float(vChange)
    
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
    
    Label(root,text="Prompt for user:).grid(row=0) ##grid sets the location
    Entry1=Entry(root,justify='center',width=10)
    Entry1.grid(row=0, column=1)
    Entry1.insert(0, 100) # set default entry as 100
    
    # Creates Button
    Single=Button(root, text="Change Intensity", bg='blue', fg='white',command=dialog) # Previously defined dialog is called here, but it doesn't necessarily have to be called
    # Set button location
    Single.grid(row=1, column=1)
    # Call the input window for display
    mainloop()
    
    
## Navigating to ImarisLib Function Documentation

Open Help > Programming Interface > Data Structures > Data Fields > All

Search through functions by letter. 

## Integrating XTension within Imaris

In the Edit menu select Menu > Preferences > Custom Tools

In the XTension Folders field, specify the folder with the XTension file by clicking on the Add button. Once the path is established, Imaris will automatically update the list of available XTensions within that folder.

## Running an XTension

Once XTension is integrated, it will automatically show up under the Image Processing tab. Click on your XTension to run it.







