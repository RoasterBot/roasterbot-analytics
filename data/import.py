import sqlite3

conn = sqlite3.connect('./main.db')

#conn.execute('select count(*) from RoastLog')
c = conn.cursor();
#c.execute('select count(*) from RoastLog')

print c.fetchone()

import csv

#with open('../logs/sqlite_import_test.log') as csvfile:
#    reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
#    for row in reader:
#        print zip ( row.keys() )
        #print ', '.join(row)
        #vals = row.itervalues()
        #print vals
        #print row.itervalues()
        #for val in row.iteritems():
        #    print val


data = []

with open('../logs/sqlite_import_test.log') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        #   print row

        date_time = row[0]
        ms = row[1]
        secs = row[2]
        ambient = row[3]
        bean = row[4]
        air = row[5]
        data.append( (date_time,secs,ambient,bean,air) ) 

print data

print 'inserting data'

c.executemany('INSERT INTO RoastLog (time_stamp, seconds, ambient_temp, bean_temp, air_temp) VALUES (?,?,?,?,?)', data)

conn.commit()


