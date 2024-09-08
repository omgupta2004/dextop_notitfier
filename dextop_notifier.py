from plyer import notification
import time

if __name__ =='__main__' :
   while True: 
    notification.notify(
        title="*** TAKE REST ***",
        message= "Rest is incredibly important for both our physical and mental well-being. It allows our bodies and minds to recharge and recover, leading to a wide range of benefits.",
        timeout=5    )
    time.sleep(10)
 

