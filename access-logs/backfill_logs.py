def month_converter(month):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sen', 'Oct', 'Nov', 'Dec']
    return months.index(month) + 1

import sys, datetime, time, os

from sqlalchemy import create_engine

def conv_log_date(x):

    parts = x.lstrip('[').split(':')

    dparts = parts[0].split('/')

    mnum = month_converter(dparts[1])

    dtobj = datetime.datetime(int(dparts[2]), mnum, int(dparts[0]), int(parts[1]), int(parts[2]), int(parts[3]) )

    epoc_time = int(time.mktime(dtobj.timetuple()))

    return epoc_time


PASS_FN = '/esg/config/.esg_pg_pass'


    
if not os.path.exists(PASS_FN):
    print ("need password readable")
    exit (-1)

f = open(PASS_FN)

passwd = f.read().strip()

db_str = ( 'postgresql://dbsuper:' + passwd + '@localhost:5432/esgcet')

db_engine = create_engine(db_str)


for line in open(sys.argv[1]):
    
    parts = line.split()
    
    url = parts[6]

    sz = 0

    if len(parts) > 8 and parts[9].isdigit():
        sz = int(parts[9])
        
    cmpstr = "/thredds/fileServer/"

    if url[0:len(cmpstr)] == cmpstr and parts[8] == "200" and sz > 0:
        
        logtime = conv_log_date(parts[3])

        result = db_engine.execute("select  id, date_fetched, success, user_id from esgf_node_manager.access_logging where url = 'http://aims3.llnl.gov" + url +  "' and success = True and xfer_size = -1")
        
        
        entry_id = 0
        delta = 0

#        print url

        arr = []
        for row in result:

            entry_id = row[0]
            delta = abs(int(row[1]) - logtime)

            
            arr.append([delta, entry_id, sz])

        if len(arr) > 0:
            sarr= sorted(arr, key = lambda entry: entry[0])

            if (sarr[0][0] < 16000):
                sz = sarr[0][2]
                entry_id = sarr[0][1]
            
                print "UPDATE esgf_node_manager.access_logging SET xfer_size =",sz," WHERE id =", entry_id, ";"





