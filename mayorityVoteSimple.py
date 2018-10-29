# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 19:02:54 2018

@author: Andres
"""


import numpy as np

# Equal weight distribution 
np.argmax(np.bincount([0, 0, 1],weights=[1, 1, 1]))

# Assigns classification accoundingly to weight distribution
np.argmax(np.bincount([0, 0, 1],weights=[0.2, 0.2, 0.6]))
