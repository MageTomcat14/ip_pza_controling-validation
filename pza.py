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

@keyword("write LED 1")
def writeLed1():
    pzaClient1 = Client(url="localhost", port=1883)
    pzaClient1.connect()

    d1 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=pzaTOPIC1, client=pzaClient1)

    d1.direction.value.set("toggle_led_1")
    time.sleep(1)
    d1.direction.pull.set("open")
    time.sleep(1)
    d1.direction.polling_cycle.set(10)
    time.sleep(1)

    # pzaClient1.disconnect()

@keyword("write LED 2")
def writeLed2():
    pzaClient2 = Client(url="localhost", port=1883)
    pzaClient2.connect()

    d2 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=pzaTOPIC2, client=pzaClient2)

    d2.direction.value.set("toggle_led_2")
    time.sleep(1)
    d2.direction.pull.set("open")
    time.sleep(1)
    d2.direction.polling_cycle.set(10)
    time.sleep(1)

    # pzaClient2.disconnect()

@keyword("write LED 16")
def writeLed16():
    pzaClient16 = Client(url="localhost", port=1883)
    pzaClient16.connect()

    d16 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=pzaTOPIC16, client=pzaClient16)

    d16.direction.value.set("toggle_led_16")
    time.sleep(1)
    d16.direction.pull.set("open")
    time.sleep(1)
    d16.direction.polling_cycle.set(10)
    time.sleep(1)

    # pzaClient16.disconnect()

@keyword("write LED 18")
def writeLed18():
    pzaClient18 = Client(url="localhost", port=1883)
    pzaClient18.connect()

    d18 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=pzaTOPIC18, client=pzaClient18)

    d18.direction.value.set("toggle_led_18")
    time.sleep(1)
    d18.direction.pull.set("open")
    time.sleep(1)
    d18.direction.polling_cycle.set(10)
    time.sleep(1)

    # pzaClient18.disconnect()