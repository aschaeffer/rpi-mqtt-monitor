from random import randrange

# MQTT server configuration
mqtt_host = "qualityland"
mqtt_user = ""
mqtt_password = ""
mqtt_port = "1883"
mqtt_topic_prefix = "/system" #qualityland"

# Messages configuration

# If this is set to True the script will send just one message containing all values
group_messages = False

# If this is set, then the script will send MQTT discovery messages meaning a config less setup in HA.  Only works for group_messages being False
discovery_messages = False

# Random delay in seconds before measuring the values
# - this is used for de-synchronizing message if you run this script on many hosts, set this to 0 for no delay.
# - if you want a fix delay you can remove the randarnge function and just set the needed delay.
random_delay = randrange(1)

# This is the time  between sending the individual messages
sleep_time = 0.1
cpu_load = True
cpu_temp = True
used_space = True
voltage = True
sys_clock_speed = True
swap = True
memory = True
uptime = True
