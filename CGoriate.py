#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 23:17:28 2023

@author: kukurihime
"""
import time
#import CTrainStatus
import CGoriateControler
#import CTrainCameraView
#import CTrainCameraMQTTSub
import CRepetationalThread


class CGoriate(CRepetationalThread.CRepetationalThread):
    def __init__(self, argv, interval = 0.1):
        super().__init__(interval)
#        self.ts = CTrainStatus.CTrainStatus(argv)
#        self.tcv = CTrainCameraView.CTrainCameraView(self.ts) #another thread
#        self.gc = CGoriateControler.CGoriateControler(self.ts)
        self.gc = CGoriateControler.CGoriateControler()
#        self.tcms = CTrainCameraMQTTSub.CTrainCameraMQTTSub(self.tc)
        
#        self.tcv.start()
        
    def func(self):
        #if not self.tcms.isConnected():
        #    print('test2')
        #    self.tcms.connect()
        
#        self.valueUpdate()
#        self.targetUpdate()
        self.execute()
#       if not self.ts.getCommand() == 'q':
#           self.setCommand( "")
    
#   def valueUpdate(self):
#       self.ts.update()
    
#    def targetUpdate(self):
#        self.tc.statusUpdate()

    def execute(self): 
        self.gc.run()
        
#    def setCommand(self, command):
#        self.command = command
#        self.tc.setCommand(command)
        
#    def getCommand(self):
#        return self.ts.getCommand()
    
#    def finish(self):
#        self.tcv.join()
    
   
    def demo(self):
        time.sleep(1)
        test = [0.5, 0.5]
        self.gc.outputPWMPair(test)
        time.sleep(5)
        
        self.gc.stopPWMPair()