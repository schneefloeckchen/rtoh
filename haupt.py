#
# Program to convert rno-like textfiles into HTML code.
#
#  Main purpose is, to make it more easy to use HTML as long lasting documentation.
#  it will use the former rno idea, to use the first character in a text line to define the tags.
# If the first character in a line is a dot, it will be a formatting command.
#
#  E.g.:
#   .ol     will start a ordered list
#   .li will define a list item
#
#
#      First commands to implement:
#  .. - double dot, if we need a dot at the start
#  .ol: ordered list
#  .li  list item
#
# 

from tkinter import Tk,  Button,  W,  E,  Entry
from pathlib import Path
import json
from datetime import datetime

class Haupt():
    """Start des Programmes, Aufbau des Bildschirmes. Dialogaufbau:
    links 4 Buttons untereinander:
        Source File,  zur Auswahl des .rno files,  Textfeld daneben zur Anzeige und
        zur manuellen Eingabe
        generate Resultfile Name: Maht aus dem .rno einen .HTML im Ausgangsfenster
        Target File: Eingabe,  Selektion des Ausgabefules,  falls der eingegebene nicht passt
        Start: Start the process
        Entries to be stored in a JSON file, in user's home, subfolder .rtoh, when Start button is pressed.
    """
    def __init__(self):
        """Im Init der Aufbau des Dialoges, Start logging
        """
        wurzel = Tk()
        wurzel.title("RNO tu HTML")
        loadButton = Button(wurzel,  text="Use File" )
        loadButton.grid(row="0",  column="0",  sticky=W+E)
        
        createOutputFileNameButton = Button(wurzel, 
                                                                              text="Create Output File Name", 
                                                                              command=self.doCreateOutputFileName)
        createOutputFileNameButton.grid(row="1",  column="0",  sticky=W+E)
        
        selectOutputFileNameButton = Button(wurzel,  text="Select Output File")
        selectOutputFileNameButton.grid(row="2",  column="0",  sticky=W+E)
        self.outputFileEntry = Entry(wurzel)
        self.outputFileEntry.grid(row=2,  column=1)
        
        createOutputFileButton = Button(wurzel,  text="Create Output File")
        createOutputFileButton.grid(row="3",  column="0",  sticky=W+E)
        
        quitButton = Button(wurzel,  text="Quit",  command=wurzel.quit)
        quitButton.grid(row="4",  column="0",  sticky=W+E)
        
        # Now get the data from last session
        vault = Vault()
        self.loadFileEntry.insert(0,  vault.getInputFileName())
        self.outputFileEntry.insert(0,  vault.getOutputFileName())
        wurzel.mainloop()
        
    def doCreateOutputFileName(self):
        inputFileName = self.loadFileEntry.get()
        print(inputFileName)
        
class Vault():
#    ""Stores the dialog values and some configuration items in a local user file.
 #  Filename is .rtoh/vault.cfg in users home""
    def __init__(self):
        print ("Init Vault")
        homePath = str(Path.home())
        self.vaultPath = homePath+"/.rtoh/vault.cfg"
        print(self.vaultPath)
        try:
          with open(self.vaultPath) as userConfigurationFile:
              self.configuration = json.load(userConfigurationFile)
        except FileNotFoundError :
            print  ("File nicht da")
            self.configuration =  {
             'input file': 'Please select', 
              'output file': 'Please select', 
              'window width':'600', 
              'window height':'400', 
              'last update':'not defined'
            }
            self.save()
            

    def setFileData(self,  inputFile,  outputFile):
        self.inputFile = inputFile
        self.outputFile = outputFile
        
    def getInputFileName(self):
        return self.configuration["input file"]

    def getOutputFileName(self):
        return self.configuration["output file"]
        
    def save(self):
        "Saves the updated configuration file"
        self.configuration['last update']=str(datetime.now())
        with open(self.vaultPath,  'w') as outputFile:
            json.dump(self.configuration,  outputFile,  indent=2)

app = Haupt()

