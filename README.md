# esgf-misc-util

Utilities for esgf use



1)  access-logs

backfill_logs.py - script takes a tomcat access log as an argument.  
                  Outputs a series of INSERT sql statements to be inserted into the esgcet database
run_log_fill.sh - intended to run as a cron to process the most recent tomcat access log.

install_log_filter.sh - to be run as root/sudo privs: sets up a cron tab (if not there already) and copies scripts to /opt/esgf/util (new place for scripts)  $ sudo bash install_log_filter.sh
