
BEGIN;


PRAGMA foreign_keys = ON;

drop table Roaster;

/**
  Represents a roasting machine -- a roaster, which is not the person
  who operates the machine. In this system that would be the roast operator.
*/
create table Roaster (
 	id INTEGER PRIMARY KEY, 
	manufacturer varchar(128),
	year INTEGER,
	model varchar(128), 
	notes text	
);


insert into Roaster 
 (manufacturer,year,model,notes)	
  values 
 ('US Roaster Corp.', 2015, '1lb Sample Roaster','Propane, black and chrome.');

drop table Bean;

create table Bean (
 id INTEGER PRIMARY KEY,
 friendly_identifier varchar NULL,
 name varchar (128),
 producer  varchar (128),
 species  varchar (128),
 varieties  varchar (128),
 harvestDate date,
 scaa_score INTEGER,
 price_per_lb numeric
);


drop table RoastLog;

CREATE TABLE RoastLog (
    id INTEGER PRIMARY KEY,
    time_stamp TIMESTAMP,
    seconds INTEGER NULL,
    batch_id INTEGER NULL,
    bean_id INTEGER NULL,
    bean_description varchar(56) NULL,
    ambient_temp INTEGER,
    bean_temp INTEGER,
    air_temp INTEGER,
    thermocouple_2_temp  INTEGER NULL,
    thermocouple_3_temp  INTEGER NULL,
    notes TEXT NULL
  );

/* --- future state
create table RoastLog (
 	id INTEGER PRIMARY KEY, 
  	batch_id INTEGER,
  	roaster_id INTEGER,
  	roaster_operator_id INTEGER FOREIGN KEY
  	order_reference varchar(56),
  	bean_id INTEGER,
  	time_stamp TIMESTAMP,
  	event_id INTEGER FOREIGN KEY, 
  	air_temp INTEGER,
  	bean_temp INTEGER,
  	ambient_temp INTEGER,
  	other_temp1  INTEGER NULL,
  	other_temp2  INTEGER NULL,
  	gas_preasure  INTEGER NULL,

  	FOREIGN KEY(roaster_id) REFERENCES Roaster(id),
  	FOREIGN KEY(bean_id) REFERENCES Bean(id)


  	);
---- */


COMMIT;