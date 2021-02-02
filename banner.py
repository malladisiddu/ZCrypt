import sys
import platform,os
from platform import system
import time
def slowprint(s):
    for c in s + '\n':
    	sys.stdout.write(c)
    	sys.stdout.flush()
    	time.sleep(4. / 100)

clear = ""
if "Linux" in platform.system():
    clear = "clear"


def banner():
    os.system('tput reset')
    print("""
<--------------->     
  <------------>         
             //         
            //            
           //          
          //                  
         //           
        //            
       //             
      //               
     <------------>   
    <---------------> 
<<ZCrypt:Basic Decryption Tool>> <<st0ic3r>>""")
