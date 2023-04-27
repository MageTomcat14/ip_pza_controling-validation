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
    # for topic in inter:
    #     logger.console(f"- {topic} => {inter[topic]['type']}")

    return pzaClient


@keyword("writting DIRECTION & STATE ${VALUE} ${GPIO} ${GPIO_IN}")
def controling(CLIENT, GPIO, GPIO_IN):

    pzaTOPICGENERAL=f"pza/my_lab_server/pza_modbus_dio/My_Input_Output_GPIO{GPIO}"
    pzaTOPICGENERAL1=f"pza/my_lab_server/pza_modbus_dio/My_Input_Output_GPIO{GPIO_IN}"

    d = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=pzaTOPICGENERAL, client=CLIENT)
    d1 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=pzaTOPICGENERAL1, client=CLIENT)
    
    logger.console(f"setting GPIO number {GPIO}")
    # d.direction.value.set(GPIO)
    d.direction.value.set("out")
    time.sleep(1)
    d.direction.pull.set("down")
    time.sleep(1)
    d.direction.polling_cycle.set(15)
    time.sleep(1)
    d.state.active.set(False)
    time.sleep(1)
    d.state.active_low.set(True)
    time.sleep(1)
    d.state.polling_cycle.set(30)
    time.sleep(1)
    if GPIO == 0 or GPIO == 10 or GPIO == 16 or GPIO == 21 or GPIO == 28:
        d1.direction.value.set("out")
        d1.direction.pull.set("down")
        d1.direction.polling_cycle.set(15)
        d1.state.active.set(False)
        d1.state.active_low.set(True)
        d1.state.polling_cycle.set(30)

    logger.console(f"getting the values of GPIO number {GPIO_IN}")
    value = d1.direction.value.get()
    logger.console(value)
    time.sleep(1)
    direction = d1.direction.pull.get()
    logger.console(direction)
    time.sleep(1)
    polling_cycle = d1.direction.polling_cycle.get()
    logger.console(polling_cycle)
    time.sleep(1)
    active = d1.state.active.get()
    logger.console(active)
    time.sleep(1)
    active_low = d1.state.active_low.get()
    logger.console(active_low)
    time.sleep(1)
    state_polling = d1.state.polling_cycle.get()
    logger.console(state_polling)
    time.sleep(1)