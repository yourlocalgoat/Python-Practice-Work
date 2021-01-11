# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 10:43:51 2021

@author: salma
"""


import numpy as np
import matplotlib.pyplot as plt

class EP():

    def equation1(self,A,f,tf):
        t = np.linspace(0, tf, 100)
        x = A * np.sin(2*np.pi*f*t)
        plt.plot(t, x)
        plt.xlabel('time')
        plt.ylabel('x(t)')
        plt.title('Results of an equation')
        plt.show()
 
    def equation2(self,c1,c2,e1,e2,tf):
        t = np.linspace(0, tf, 100)
        x = c1 * np.exp(-e1*t) * np.sin(2 * t) + c2 * np.exp(-e2*t) * np.cos(2 * t)
        plt.plot(t, x)
        plt.xlabel('time')
        plt.ylabel('x(t)')
        plt.title('Results of an equation')
        plt.show()
        
