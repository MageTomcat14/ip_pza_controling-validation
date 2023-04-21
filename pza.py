from robot.api.deco import keyword
from robot.api import logger
from panduza import Dio, Client
import time

BROKER_ADDR="localhost"
BROKER_PORT=1883
CHECK_USER_INPUT=True
RUN_TEST=False


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


@keyword("writting LED ${VALUE} ${GPIO}")
def controlingLEDs(CLIENT, GPIO):

    pzaTOPICGENERAL=f"pza/my_lab_server/pza_modbus_dio/My_Input_Output_GPIO{GPIO}"
    d = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=pzaTOPICGENERAL, client=CLIENT)
    
    d.direction.value.set(f"toggle_led_{GPIO}")
    time.sleep(1)
    d.direction.pull.set("open")
    time.sleep(1)
    d.direction.polling_cycle.set(10)
    time.sleep(1)
