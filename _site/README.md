
Phidget Coffee Temperature Logging Origin Source Bikes Data Analyitics
===

## Visualise a roast in real-time from anywhere on any device

What should the interface be?  What works for me?

Should it be a web interface or command-line or both?

Should run locally and asynchronously synch up to network cloud. Ideally, a roast can be viewed by anyone in real-time. 

The software allows for specifying custom events in addition to those common in industry; e.g., first crack, second crack, etc.

---------

Story 1
As a roaster, I want to specify what beans I'm roasting and some meta data about the roast, including charge weight, machine, ambient conditions, customer or order reference, and notes about the goals of the roast.  

:: Story 1 Scenario ::
Assuming the machine is warmed up, some amount of beans are in the hopper, and the software is "ready". 

 - I "start a roast"
 - The software prompts me to specify the following:
 	- bean info (type and weight)
 	- customer info
(The software has some defaults set, assuming certain consistent behaviors.  These include the Roaster Operator info and Roaster Info.  Those can be changed at any time.)
	- Goals (This can be free form text describing what the intent of this roast is. This can be anything from sample roasting to roasting N number of batches for someone)
- I charge the roaster and tell the software to "charge", or start the actual roasting. 
	- The software displays the temperatures from each of the available temperature sensors every second.
	- The software expects to receive notification from me for the following events in this order:
	   - charge (already done), whiting, yellowing, browning, 1st crack start, 1st crack high, 1st crack end, 2nd crack start, 2nd crack high, drop, cooling end (end of roast).  Note: "drop" should be bale to be fired at any time, and if it's a mistake, can be undone. 
	   


