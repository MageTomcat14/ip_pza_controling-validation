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



@keyword("writting DIRECTION & STATE of output ${CLIENT} ${GPIO} ${GPIO_IN}")
def setting(CLIENT, GPIO, GPIO_IN):

    pzaTOPICGENERAL=f"pza/lab_paul/driver_of_PaulFisher/control_paul_IO{GPIO}"
    pzaTOPICGENERAL1=f"pza/lab_paul/driver_of_PaulFisher/control_paul_IO{GPIO_IN}"

    d = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=pzaTOPICGENERAL, client=CLIENT)
    d1 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=pzaTOPICGENERAL1, client=CLIENT)
    
    while True : 
        d.direction.value.set("out")
        time.sleep(1)
        d.direction.pull.set("up")
        time.sleep(1)
        d.direction.polling_cycle.set(1)
        time.sleep(1)

        d.state.active_low.set(False)
        time.sleep(1)
        d.state.active.set(True)
        time.sleep(1)
        logger.console(d1.state.active.get())
        time.sleep(2)
        d.state.active.set(False)
        time.sleep(1)
        d.state.polling_cycle.set(1)
        time.sleep(1)
        logger.console(d1.state.active.get())
