# esgf-misc-util

Utilities for esgf use

1)  backfilling logs

backfill_logs.py - script takes a tomcat access log as an argument.  
                  Outputs a series of INSERT sql statements to be inserted into the esgcet database
run_log_fill.sh - intended to run as a cron to process the most recent tomcat access log.
