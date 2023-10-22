#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 23:17:28 2023

@author: kukurihime
"""
import time
import CGoriateControler
import CControlLoop
import CVL53L0X
import CI2cRPi

class CGoriate(CControlLoop.CControlLoop):
    def __init__(self,  expectedLoopTime = 0.1):
        super().__init__(expectedLoopTime)
        self.gc = CGoriateControler.CGoriateControler()
        self.sensorCluster = CVL53L0X.CVL53L0X(CI2cRPi.CI2cRPi(busId = 1, i2cAddress = CVL53L0X.i2cDefaultAddress(), rate = 115200))
        self.sensorCluster.initialize()
        
    def loopFunc(self):
        res = ""
        distance = self.sensorCluster.getCategoryVal('distance')
        dist = distance[0]
        print (dist)
        if dist > 1.024:
            if not dist > 2.048:
                test = [0.9, 0.9]
                self.gc.outputPWMPair(test)
                res = "2.048 < dist"
            else:
                self.gc.stopPWMPair()
                res = "1.024 < dist < 2.048"
        else:
            if dist < 0.128:
                test = [-0.9, -0.9]
                self.gc.outputPWMPair(test)
                res = "dist < 0.128"
            else:
                self.gc.stopPWMPair()
                res = "0.128 < dist < 1.024"
                
        print(res)
                
        
    def postProcess(self): 
        pass
    
    
    
    def demo(self):
        time.sleep(1)
        test = [0.9, 0.9]
        self.gc.outputPWMPair(test)
        
        test = [0.9, 0.9]
        self.gc.outputPWMPair(test)
        
        time.sleep(5)
        
        self.gc.stopPWMPair()
        
if __name__ == '__main__':
    goriate = CGoriate()
    goriate.start()
    