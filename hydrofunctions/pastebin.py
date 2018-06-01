# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 10:45:29 2018

@author: Marty

pastebin.py

This file is not meant to be included in any merge with Develop!
As the name implies, this is just a dump where I can store useful code
from my notebooks in one central location for later development.

1) Paste new code from the notebooks into this module.

2) If I choose to develop some code further:
    - move it into an official module
    - add tests
    - add documentation & example notebooks
    ==> OPTION 1: create a branch off of paste-bin with a descriptive name
            - delete this module (pastebin.py)
            - merge the new branch with the Develop branch
            - Keep adding stuff to the paste-bin branch; repeat
    ==> OPTION 2: Create a branch off of Develop
            - Cut and paste new files and modules from paste-bin branch into the new branch
            - Keep adding stuff to the paste-bin branch; repeat
"""

def cleanDF(DF):
    DF = pd.DataFrame(DF.iloc[:,0])
    cols = DF.columns.values
    for i, col in enumerate(cols):
        cols[i] = col[5:-12] # This works for siteID's of different lengths.
    DF.columns = cols
    print(DF.columns)
    return DF
