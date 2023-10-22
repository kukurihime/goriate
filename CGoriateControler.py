#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 23:20:51 2023

@author: kukurihime
"""
import CRPiControler
import time

class CGoriateControler:
    def __init__(self):

        self.speedTable = { \
                           -1:(0.0, 0.6), \
                           0:(0.0, 0.0), \
                           1:(0.6, 0.0), \
                           2:(0.7, 0.0), \
                           3:(0.8, 0.0), \
                           4:(0.9, 0.0), \
                           5:(1.0, 0.0)
                           }
        self.maxSpeed = 5
        self.minSpeed = -1
        self.rpcMode = True #full functional mode

        
        self.rpc = CRPiControler.CRPiControler(self.rpcMode)
        self.rpc.ready()

    def statusUpdate(self): 
        pass
    
    def run(self):
        pass
        
    def stop(self):
        self.rpc.pwmStop(self.rpc.leftPWM)
        self.rpc.pwmStop(self.rpc.rightPWM)
        self.rpc.off(self.rpc.leftD)
        self.rpc.off(self.rpc.rightD)
    
    def setTargetSpeed(self, num):
        if type(num) is not int:
            return
        
        if num > self.maxSpeed:
            num = self.maxSpeed
        elif num < self.minSpeed:
            num = self.minSpeed
        
        self.ts.setTargetAt(0, num)
                
    def outputPWMPair(self, PWMPair):
        self.rpc.pwmOutput(self.rpc.leftPWM, PWMPair[0])
        self.rpc.pwmOutput(self.rpc.rightPWM, PWMPair[1])
        
    def forword(self):
        self.rpc.on(self.rpc.leftD)
        self.rpc.pwmOutput(self.rpc.leftPWM, 0.9)
        
    def stopPWMPair(self):
        self.rpc.pwmStop(12)
        self.rpc.pwmStop(13)
        
if __name__ == "__main__":
    gc = CGoriateControler()
    gc.forword()
    time.sleep(5)
    gc.stop()
        