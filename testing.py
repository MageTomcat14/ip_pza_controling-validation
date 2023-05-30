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

    return pzaClient

@keyword("declaring topics and instances ${CLIENT} ${GPIO} ${GPIO_IN}")
def declareTopics(CLIENT, GPIO, GPIO_IN):

    pzaTOPICGENERAL_OUT=f"pza/lab_paul/io_pza_controling/testing_of_io_controling-{GPIO}"
    pzaTOPICGENERAL_IN=f"pza/lab_paul/io_pza_controling/testing_of_io_controling-{GPIO_IN}"

    d = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=pzaTOPICGENERAL_OUT, client=CLIENT)
    d1 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=pzaTOPICGENERAL_IN, client=CLIENT)

    return d, d1


@keyword("setting IO ${GPIO_OUT} to output ${INSTANCE_OUT}")
def setOutput(GPIO_OUT, INSTANCE_OUT):
    logger.console(f"setting IO {GPIO_OUT} to output")
    INSTANCE_OUT.direction.value.set("out")

@keyword("setting IO ${GPIO_IN} to input ${INSTANCE_IN}")
def setInput(GPIO_IN, INSTANCE_IN):
    logger.console(f"setting IO {GPIO_IN} to input")
    INSTANCE_IN.direction.value.set("in")



@keyword("setting pull of ${GPIO} ${INSTANCE_IN}")
def settingPullInput(GPIO, INSTANCE_IN):
 
    logger.console(f"setting the pull of the input IO {GPIO}")
    INSTANCE_IN.direction.pull.set("down")



@keyword("setting pulling cycle of IO ${GPIO} and ${GPIO_OUT} ${INSTANCE_OUT} ${INSTANCE_IN}")
def settingPullingCycle(GPIO, GPIO_OUT, INSTANCE_OUT, INSTANCE_IN):


    logger.console(f"setting the pulling cycle of IO {GPIO_OUT} and {GPIO}")

    INSTANCE_OUT.direction.polling_cycle.set(0.5)
    INSTANCE_OUT.state.polling_cycle.set(0.5)
    INSTANCE_IN.direction.polling_cycle.set(0.5)
    INSTANCE_IN.state.polling_cycle.set(0.5)


@keyword("setting active state low ${INSTANCE_OUT} ${INSTANCE_IN}")
def settingActiveLow(INSTANCE_OUT, INSTANCE_IN):

    logger.console("setting the active state low")
    INSTANCE_OUT.state.active_low.set(False)


@keyword("setting IO ${GPIO} to true ${INSTANCE_OUT}")
def settingToTrue(GPIO, INSTANCE_OUT):
    logger.console(f"setting IO {GPIO} to True")
    INSTANCE_OUT.state.active.set(True)
    time.sleep(1)


@keyword("setting IO ${GPIO} to False ${INSTANCE_OUT}")
def settingToTrueFalse(GPIO, INSTANCE_OUT):
    logger.console(f"setting IO {GPIO} to False")
    INSTANCE_OUT.state.active.set(False)
    time.sleep(1)


@keyword("getting the value of IO ${GPIO} ${INSTANCE_IN}")
def getValue(GPIO, INSTANCE_IN):
    logger.console(f"get the value of IO {GPIO}")
    result = INSTANCE_IN.state.active.get()
    logger.console(result)
    time.sleep(1)

@keyword("configure pulls to a output ${GPIO} ${INSTANCE_OUT}")
def errorPULL(GPIO, INSTANCE_OUT):
    logger.console(f"check error pull {GPIO}")
    INSTANCE_OUT.direction.pull.set("down")

@keyword("write to a input ${GPIO} ${INSTANCE_IN}")
def errorWRITE(GPIO, INSTANCE_IN):
    logger.console(f"check error write {GPIO}")
    INSTANCE_IN.state.active.set(True)

@keyword("ending")
def end():
    
    logger.console("TEST ARE DONE")