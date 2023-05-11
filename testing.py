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

@keyword("declaring topics and instances ${CLIENT} ${GPIO} ${GPIO_IN}")
def declareTopics(CLIENT, GPIO, GPIO_IN):

    pzaTOPICGENERAL_OUT=f"pza/lab_paul/io_pza_controling/testing_of_io_controling{GPIO}"
    pzaTOPICGENERAL_IN=f"pza/lab_paul/io_pza_controling/testing_of_io_controling{GPIO_IN}"

    d = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=pzaTOPICGENERAL_OUT, client=CLIENT)
    d1 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=pzaTOPICGENERAL_IN, client=CLIENT)

    return d, d1

@keyword("writting DIRECTION of IO ${INSTANCE_OUT} ${INSTANCE_IN}")
def settingDir(INSTANCE_OUT, INSTANCE_IN):

    logger.console("setting the direction of the IO")
    INSTANCE_OUT.direction.value.set("out")
    INSTANCE_IN.direction.value.set("in")

@keyword("setting pulls ${INSTANCE_OUT} ${INSTANCE_IN}")
def settingPulls(INSTANCE_OUT, INSTANCE_IN):
 
    logger.console("setting the pulls")
    INSTANCE_OUT.direction.pull.set("up")
    INSTANCE_IN.direction.pull.set("down")


@keyword("setting pulling cycle ${INSTANCE_OUT} ${INSTANCE_IN}")
def settingPullingCycle(INSTANCE_OUT, INSTANCE_IN):


    logger.console("setting the pulling cycle")
    INSTANCE_OUT.direction.polling_cycle.set(0.1)
    INSTANCE_OUT.state.polling_cycle.set(0.1)
    INSTANCE_IN.direction.polling_cycle.set(0.1)
    INSTANCE_IN.state.polling_cycle.set(0.1)

@keyword("setting active state low ${INSTANCE_OUT} ${INSTANCE_IN}")
def settingActiveLow(INSTANCE_OUT, INSTANCE_IN):

 
    logger.console("setting the active state low")
    INSTANCE_OUT.state.active_low.set(False)
    INSTANCE_IN.state.active_low.set(False)


@keyword("writting to output and getting the input ${INSTANCE_OUT} ${INSTANCE_IN}")
def writtingOutput(INSTANCE_OUT, INSTANCE_IN):


    logger.console("setting writting the IO")
    INSTANCE_OUT.state.active.set(True)
    time.sleep(1)
    result = INSTANCE_IN.state.active.get()
    logger.console(result)
    time.sleep(1)
    INSTANCE_OUT.state.active.set(False)
    time.sleep(1)
    result = INSTANCE_IN.state.active.get()
    logger.console(result)