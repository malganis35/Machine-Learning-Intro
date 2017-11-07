# -*- coding: utf-8 -*-
"""
Created on Tue Nov 07 17:56:05 2017

@author: caotrido
"""
import os
# Create a dictionary to store user parameters
PATH = {}
PATH["parent"] = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
PATH["data"] = PATH["parent"] + "/01_PBC/2 - Iris/"

PARAM = {}
PARAM["fileData"] = "IRIS.csv"
PARAM["separator"]= ","
PARAM["encoding"] = "utf-8" # ce paramètre est super important quand on lit des fichiers texte sinon tu vas avoir des bugs ....

#%%
import pandas as pd

filename = PATH["data"] + PARAM["fileData"] # full path of my data
df = pd.read_csv(filename, sep = PARAM["separator"], encoding = PARAM["encoding"])

print df