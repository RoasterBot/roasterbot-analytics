
BEGIN;


PRAGMA foreign_keys = ON;


/*----------------------------------*/

DROP TABLE RoastLog;

CREATE TABLE RoastLog (
    id INTEGER PRIMARY KEY,
    time_stamp TIMESTAMP,
    seconds INTEGER NULL,
    batch_id INTEGER NULL,
    ambient_temp INTEGER,
    bean_temp INTEGER,
    air_temp INTEGER,
    thermocouple_2_temp  INTEGER NULL,
    thermocouple_3_temp  INTEGER NULL
  );



/*----------------------------------*/

DROP TABLE BatchInfo;

CREATE TABLE BatchInfo (
    id INTEGER PRIMARY KEY,
    bean_id INTEGER,
    amount INTEGER,
    notes TEXT NULL,
    cupping_notes TEXT NULL
);

/*----------------------------------*/

DROP TABLE Bean;
CREATE TABLE Bean (
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


/*----------------------------------*/

DROP TABLE Roaster;

CREATE TABLE Roaster (
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


COMMIT;

