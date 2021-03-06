export PGPASSWORD=`cat /esg/config/.esg_pg_pass`

source /etc/esg.env


fn=`ls -trl /usr/local/tomcat/logs/localhost_access_log..20*.txt | tail -n 2 | head -n 1 | awk '{print $9}'`
echo $fn

python /opt/esgf/util/backfill_logs.py $fn  > /tmp/logtmp.sql

psql -U dbsuper esgcet < /tmp/logtmp.sql