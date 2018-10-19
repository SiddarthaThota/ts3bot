import ts3
import time
import thread

URI = "ssh://serveradmin:Z0YxRb7u@localhost:10022"
SID = 1

def keepAlive(ts3conn):
    while true:
        ts3conn.send_keepalive()
        time.sleep(300)

with ts3.query.TS3ServerConnection(URI) as ts3conn:
    ts3conn.exec_("use", sid=SID)    
    thread.start_new_thread(keepAlive(ts3conn))
