#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 22:53:54 2023

@author: kukurihime
"""


import CGoriate
#import CRealtimeKeyInput
import time
import sys


print("goriate Start!!")
time.sleep(0.5)

argv = sys.argv
#if len( argv ) == 1:
#    argv.append("real") 

go = CGoriate.CGoriate(0.1)
#go.start() #other thread
go.loopStart()


#command proccess loop
#rki = CRealtimeKeyInput.CRealtimeKeyInput()
#rki.setDaemon(True)
#rki.start()
#key = ''
#while not key == 'q':
#    if rki.hasNewKey():
#        key = rki.getKey()
#        cg.setCommand(key)
#    else:
#        key = cg.getCommand()
    #print("key:", key)
#    if key == 'q':
#        rki.stop()
#        pass
#        
#    time.sleep(0.1)
    
        

print( "quit command")
#rki.finish()
#go.finish()
#go.join()

print("goriate Finished!!")



