export PGPASSWORD=`cat /esg/config/.esgf_pg_pass`


fn=`ls -trl /usr/local/tomcat/logs/ | tail -n 1 | awk '{print $9}'`


echo time python backfill_logs.py $fn 
#> /tmp/logtmp.sql

#echo time psql -U dbsuper esgcet 
#< /tmp/logtmp.sql