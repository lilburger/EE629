# -*- coding: utf-8 -*-



"""
import os
import time

# loop
while: 
# read time information
    time_str = time.strftime('%Y-%m-%d %H:%M：%S'mtime,localtime(time.time())) 
# read CPU temperature digital information
    file = open("/sys/class/thermal/thermal_zone0/temp") 
# make the temperature readable
    temp = float(file.read()) / 1000 
    mail = "echo ' %s CPUtemperature%.2f℃ ' |mutt -s 'CPU temperatuer warning' 1347173703@qq.com" % ti$
    
    a = 60 #given the warning temperature 60 degrees
    
# if the temperature of cpu is higher than a,then send the email  
    if float(temp)>float(a):  
# send email
        os.system(mail) 
# if the condition is satisfied, then loop stopped
        break
# if the temperature<60, then wait 3 second to start a next loop
    time.sleep(3)
    
    