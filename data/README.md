README
====


Schema, Data Dictionary, DDL statements


Tables
=====

- Customer
 - name
 - email
 - twitter
 - cell

- Company
  - name
  - street
  - city
  - state
  - zip
  - country
  - phone
  - www

- RoasterOperator
  - id
  - company_id
  - name
  - email
  - cell


- Roaster
 - Manufacturer
 - Year
 - Model
 - Capacity
 - Notes


 - BeanInfo
   - id
   - User-defined identifier (optional)
   - Name
   - Region
   - Producer (Farm)
   - Species
   - Varieties
   - HarvestDate
   - SCA_score
   - price_per_lb (don't need both)
   - price_per_kilo

  - RoastEvent
   - id
   - type (charge, yellow, brown, 1st crack start, 1st crack high, 1c stop, dev time, 2c start, 2c high, drop.  Should also allow for custom event tracking)
  	   :: Note :: visualize as color change in background of chart; e.g., green, white-ish, yellow, tan, brown, dark brown, ..., black
  	- description

  - RoastLog
  	- id
  	- batch_id
  	- roaster_id
  	- roaster_operator_id
  	- order_reference (for specific customer)
  	- bean_id (fk)
  	- Date-time stamp
  	- event_id 
  	- air_temp
  	- bean_temp
  	- ambient_temp
  	- other_temp1 (if there are other thermocouples)
  	- other_temp2 ('')
  	- other_metric (e.g., gas pressure)


  - CuppingNotes
   - id
   - roast_id
   - notes
   - score
   - tastify_url








