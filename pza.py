from robot.api.deco import keyword
from robot.api import logger
from panduza import Dio, Client
import time

BROKER_ADDR="localhost"
BROKER_PORT=1883
CHECK_USER_INPUT=True
RUN_TEST=False

var1 = 1
var2 = 2
var16 = 16
var18 = 18

# one topic per io
logger.console("declaring the topics ...")
pzaTOPIC1=f"pza/my_lab_server/pza_modbus_dio/My_Input_Output_GPIO{var1}"
pzaTOPIC2=f"pza/my_lab_server/pza_modbus_dio/My_Input_Output_GPIO{var2}"
pzaTOPIC16=f"pza/my_lab_server/pza_modbus_dio/My_Input_Output_GPIO{var16}"
pzaTOPIC18=f"pza/my_lab_server/pza_modbus_dio/My_Input_Output_GPIO{var18}"


@keyword("connect to client and MQTT")
def init():
    pzaClient = Client(url="localhost", port=1883)
    pzaClient.connect()

    # scan the interface
    inter = pzaClient.scan_interfaces()

    # list all the topics
    logger.console("scanning the interfaces..")
    for topic in inter:
        logger.console(f"- {topic} => {inter[topic]['type']}")

    return pzaClient

@keyword("write LED 1 ${VALUE}")
def writeLed1(VALUE):

    d1 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=pzaTOPIC1, client=VALUE)

    d1.direction.value.set("toggle_led_1")
    time.sleep(1)
    d1.direction.pull.set("open")
    time.sleep(1)
    d1.direction.polling_cycle.set(10)
    time.sleep(1)

@keyword("write LED 2 ${VALUE}")
def writeLed2(VALUE):

    d2 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=pzaTOPIC2, client=VALUE)

    d2.direction.value.set("toggle_led_2")
    time.sleep(1)
    d2.direction.pull.set("open")
    time.sleep(1)
    d2.direction.polling_cycle.set(10)
    time.sleep(1)

@keyword("write LED 16 ${VALUE}")
def writeLed16(VALUE):


    d16 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=pzaTOPIC16, client=VALUE)

    d16.direction.value.set("toggle_led_16")
    time.sleep(1)
    d16.direction.pull.set("open")
    time.sleep(1)
    d16.direction.polling_cycle.set(10)
    time.sleep(1)


@keyword("write LED 18 ${VALUE}")
def writeLed18(VALUE):

    d18 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=pzaTOPIC18, client=VALUE)
    
    d18.direction.value.set("toggle_led_18")
    time.sleep(1)
    d18.direction.pull.set("open")
    time.sleep(1)
    d18.direction.polling_cycle.set(10)
    time.sleep(1)
