#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pigpio
import time

class CRPiControler:
        def __init__(self, mode):
            self.dummyFlg = not mode #True:with pigpiod, False:without pigpiod
            if not self.dummyFlg:
                self.pi = pigpio.pi()
                
            self.leftD = 16
            self.leftPWM = 12 #hardwarePWM0
            self.rightPWM = 13 #hardwarePWM1
            self.rightD = 20 #LED

            self.H = 1
            self.L = 0
                
            self.freq = 10000 #PWMFrequency
            self.raspberryPiPWMValue = 1000000 #raspberryPi PWM
            
        def ready(self):
            if self.dummyFlg:
                return
            self.pi.set_mode(self.leftD, pigpio.OUTPUT)
            self.pi.set_mode(self.leftPWM, pigpio.ALT0)
            self.pi.set_mode(self.rightPWM, pigpio.ALT0)
            self.pi.set_mode(self.rightD, pigpio.OUTPUT)

            self.off(self.leftD)
            self.off(self.leftPWM)
            self.off(self.rightPWM)
            self.off(self.rightD)
            
        def finish(self):
            if self.dummyFlg:
                return
            
            self.PWMStop(self.leftPWM)
            self.PWMStop(self.rightPWM)
            time.sleep(1)
            self.off(self.leftD)
            self.off(self.rightD)
        
            self.pi.set_mode(self.leftD, pigpio.INPUT)
            self.pi.set_mode(self.leftPWM, pigpio.INPUT)
            self.pi.set_mode(self.rightPWM, pigpio.INPUT)
            self.pi.set_mode(self.rightD, pigpio.INPUT)
            self.pi.stop()

        def PWMDuty(self, dutyRatio):
            return int(self.raspberryPiPWMValue * dutyRatio)
        
        def pwmOutput(self, pin, dutyRatio):
            if self.dummyFlg:
                return
            
            self.pi.hardware_PWM(pin, self.freq, self.PWMDuty(dutyRatio))
        
        def pwmStop(self, pin):
            if self.dummyFlg:
                return
            
            self.pi.hardware_PWM(pin, self.freq, 0)
        
        def on(self, pin):
            if self.dummyFlg:
                return
            
            self.pi.write(pin, self.H)
            
        def off(self, pin):
            if self.dummyFlg:
                return
            self.pi.write(pin, self.L)