# Troubleshooting

This document collects some problems that might occur to you, and provides a possible solutions for them.

## Elasticsearch cannot be started

*This description is presented for Linux.*

```bash
Job for elasticsearch.service failed because the control process exited with error code.
See "systemctl status elasticsearch.service" and "journalctl -xeu elasticsearch.service" for details.
```

If you get the following error: `elasticsearch.service: Failed with result 'oom-kill'.` you should adjust the heap memory for the JVM running the Elasticsearch server. For that do the following steps:

```bash
# open the jvm.options file for editing
sudo vi /etc/elasticsearch/jvm.options

# un-comment the values of -Xms and -Xmx and set for both of the a reasonable size, e.g.:
-Xms512m
-Xmx512m

# restart the service again
sudo service elasticsearch restart

# you can check the service status any time vy calling
sudo service elasticsearch status
```

## Elasticsearch is available but indexer gets connection error

*This description is presented for Windows.*

Elasticsearch needs you to have 10% free space on your disk by default. One possible cause of this error, is that you have less space available. 

To check whether this is the problem, look at bottom of `%ES_HOME%\logs\elasticsearch.log`. You should see an error `high disk watermark [90%] exceeded`. You can either free up space on your disk or change the `disk watermark` settings of your cluster.
