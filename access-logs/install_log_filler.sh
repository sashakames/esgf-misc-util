
# must run as root

mkdir -p /opt/esgf/util


cp run_log_fill.sh /opt/esgf/util
cp backfill_logs.py /opt/esgf/util

chmod -R a+rx /opt/esgf/util

val=`grep run_log_fill /var/spool/cron/root | wc -l`

if [ $val -eq 0 ] ; then 
    echo "15 3 * * * bash /opt/esgf/util/run_log_fill.sh" >> /var/spool/cron/root

fi
