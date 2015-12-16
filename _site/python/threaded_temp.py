#! /usr/bin/env python
# -*- codes: utf-8 -*-

print 'Starting ...'

#Basic imports
from ctypes import *
import sys
import time
import threading
import logging
#Phidget specific imports
from Phidgets.PhidgetException import PhidgetErrorCodes, PhidgetException
from Phidgets.Events.Events import AttachEventArgs, DetachEventArgs, ErrorEventArgs, TemperatureChangeEventArgs
from Phidgets.Devices.TemperatureSensor import TemperatureSensor, ThermocoupleType
#import methods for sleeping thread
from time import sleep
from Phidgets.Phidget import PhidgetLogLevel


#Information Display Function
def DisplayDeviceInfo():
    inputCount = temperatureSensor.getTemperatureInputCount()
    print("|------------|----------------------------------|--------------|------------|")
    print("|- Attached -|-              Type              -|- Serial No. -|-  Version -|")
    print("|------------|----------------------------------|--------------|------------|")
    print("|- %8s -|- %30s -|- %10d -|- %8d -|" % (temperatureSensor.isAttached(), temperatureSensor.getDeviceName(), temperatureSensor.getSerialNum(), temperatureSensor.getDeviceVersion()))
    print("|------------|----------------------------------|--------------|------------|")
    print("Number of Temperature Inputs: %i" % (inputCount))
    for i in range(inputCount):
        print("Input %i Sensitivity: %f" % (i, temperatureSensor.getTemperatureChangeTrigger(i)))

#Event Handler Callback Functions
def TemperatureSensorAttached(e):
    attached = e.device
    print("TemperatureSensor %i Attached!" % (attached.getSerialNum()))

def TemperatureSensorDetached(e):
    detached = e.device
    print("TemperatureSensor %i Detached!" % (detached.getSerialNum()))

def TemperatureSensorError(e):
    try:
        source = e.device
        if source.isAttached():
            print("TemperatureSensor %i: Phidget Error %i: %s" % (source.getSerialNum(), e.eCode, e.description))
    except PhidgetException as e:
        print("Phidget Exception %i: %s" % (e.code, e.details))


# Event-based. Change to timer-based. Once per second.
def TemperatureSensorTemperatureChanged(e):
    try:
        ambient = temperatureSensor.getAmbientTemperature() #
    except PhidgetException as e:
        print("Phidget Exception %i: %s" % (e.code, e.details))
        ambient = 0.00
    
    source = e.device
    #print("TemperatureSensor %i: Ambient Temp: %f -- Thermocouple %i temperature: %f -- Potential: %f" % (source.getSerialNum(), ambient, e.index, e.temperature, e.potential))
    #print temperatureSensor.getTemperature(0)*2+30
    print 'Time: %s.  Device %s. Current temp (F): %f' % (time.time()-start_time, e.index, toFarenheight(e.temperature) )
    # Format, date, thermocouple, time, thermocouple temp, ambient temp at device
    logging.info( "%s,%s,%f" % (time.time()-start_time, e.index, toFarenheight(e.temperature) ))


def toFarenheight(c):
    # from MAX3865 code
    # and http://www.almanac.com/temperature-conversion
    #  temperature = (temperature * 9.0/5.0)+ 32;
    #return c*2+30
    return  c * (9.0/5.0)+ 32;

def log_temperatures():

    print 'logging'

    
    # Rethinking exception handling ... ?
    try:
        ambient_temp = temperatureSensor.getAmbientTemperature() #
    except PhidgetException as e:
        print("Phidget Exception %i: %s" % (e.code, e.details))
        ambient_temp = 0.00
    
    ambient_temp =  toFarenheight( temperatureSensor.getAmbientTemperature() )
    bean_temp    =  toFarenheight( temperatureSensor.getTemperature(0) )
    air_temp     =  toFarenheight( temperatureSensor.getTemperature(1) )
    # Not using these inputs yet.
    tbd_1_temp   =  toFarenheight( temperatureSensor.getTemperature(2) )
    tbd_2_temp   =  toFarenheight( temperatureSensor.getTemperature(3) )
    c_time = time.time()-start_time

    # Format
    #logging.info("time,ambient_temp,thermocouple_0_temp,thermocouple_1_temp,thermocouple_2_temp,thermocouple_3_temp")

    print ( "%d seconds, ambient_temp=%d, bean_temp=%d, air_temp=%d, tbd1=%d, tbd2=%d" % (c_time, ambient_temp, bean_temp, \
                                air_temp, tbd_1_temp, tbd_2_temp ))
    logging.info( "%d,%d,%d,%d,%d,%d" % (c_time, ambient_temp, bean_temp, \
                                air_temp, tbd_1_temp, tbd_2_temp ))

    return 0
    


def start_threads():
    t = threading.Timer(1.0, start_threads)
    t.daemon = True
    t.start()
    log_temperatures()

# if __name__ == '__main__':
# This is where we should start the timer and simply use
# temperatureSensor.getTemperature(0..3)


if __name__ == '__main__':
    print 'in main().'
    #The begining of the roast
    # Will need multiple "time markers" or events: Roaster warm up, drop, 1c, etc. 
    start_time = time.time()
    #need to generate unique file name for each roast ...?
    #logging.basicConfig(format='%(asctime)s,%(message)s',filename='roast.log',filemode='w',level=logging.DEBUG)

    logging.basicConfig(format='%(asctime)s,%(message)s',filename='roast.log',filemode='w',level=logging.DEBUG)

    #logging.basicConfig(format='%(message)s',filename='roast.log',filemode='w',level=logging.DEBUG)
    # Format, date, thermocouple, time, thermocouple temp, ambient temp at device
    logging.info("datetime,ms,seconds,ambient_temp,thermocouple_0_temp,thermocouple_1_temp,thermocouple_2_temp,thermocouple_3_temp")
    
    #Create an temperaturesensor object
    try:
        print 'creating temp sensor'
        temperatureSensor = TemperatureSensor()
    except RuntimeError as e:
        print("Runtime Exception: %s" % e.details)
        print("Exiting....")
        exit(1) 
   
    #start_threads()

    
    print("Opening phidget object....")
    try:
        temperatureSensor.openPhidget()
    except PhidgetException as e:
        print("Phidget Exception %i: %s" % (e.code, e.details))
        print("Exiting....")
        exit(1)

    print("Waiting for attach....")

    try:
        temperatureSensor.waitForAttach(10000)
    except PhidgetException as e:
        print("Phidget Exception %i: %s" % (e.code, e.details))
        try:
            temperatureSensor.closePhidget()
        except PhidgetException as e:
            print("Phidget Exception %i: %s" % (e.code, e.details))
            print("Exiting....")
            exit(1)
        print("Exiting....")
        exit(1)
    else:
        DisplayDeviceInfo()

    print("Setting Thermocouple type...")
    temperatureSensor.setThermocoupleType(0, ThermocoupleType.PHIDGET_TEMPERATURE_SENSOR_K_TYPE)

    print("Setting sensitivity of the thermocouple....")
    temperatureSensor.setTemperatureChangeTrigger(0, 0.10)
    sleep(5) #sleep for 5 seconds
    print("Sensitivity of thermocouple index 0 is now %f" % (temperatureSensor.getTemperatureChangeTrigger(0)))

    print("Press Enter to quit....")


    start_threads()

    chr = sys.stdin.read(1)
    print("Closing...")

    try:
        temperatureSensor.closePhidget()
    except PhidgetException as e:
        print("Phidget Exception %i: %s" % (e.code, e.details))
        print("Exiting....")
        exit(1)

    print("Done.")
    exit(0)



