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




@keyword("writting DIRECTION of IO ${CLIENT} ${GPIO} ${GPIO_IN}")
def settingDir(CLIENT, GPIO, GPIO_IN):

    pzaTOPICGENERAL=f"pza/lab_paul/io_pza_controling/testing_of_io_controling{GPIO}"
    pzaTOPICGENERAL1=f"pza/lab_paul/io_pza_controling/testing_of_io_controling{GPIO_IN}"

    d = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=pzaTOPICGENERAL, client=CLIENT)
    d1 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=pzaTOPICGENERAL1, client=CLIENT)
    
    logger.console("setting the direction of the IO")
    d.direction.value.set("out")
    d1.direction.value.set("in")

@keyword("setting pulls ${CLIENT} ${GPIO} ${GPIO_IN}")
def settingPulls(CLIENT, GPIO, GPIO_IN):

    pzaTOPICGENERAL=f"pza/lab_paul/io_pza_controling/testing_of_io_controling{GPIO}"
    pzaTOPICGENERAL1=f"pza/lab_paul/io_pza_controling/testing_of_io_controling{GPIO_IN}"

    d = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=pzaTOPICGENERAL, client=CLIENT)
    d1 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=pzaTOPICGENERAL1, client=CLIENT)
    
    logger.console("setting the pulls")
    d.direction.pull.set("up")
    d1.direction.pull.set("down")


@keyword("setting pulling cycle ${CLIENT} ${GPIO} ${GPIO_IN}")
def settingPullingCycle(CLIENT, GPIO, GPIO_IN):

    pzaTOPICGENERAL=f"pza/lab_paul/io_pza_controling/testing_of_io_controling{GPIO}"
    pzaTOPICGENERAL1=f"pza/lab_paul/io_pza_controling/testing_of_io_controling{GPIO_IN}"

    d = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=pzaTOPICGENERAL, client=CLIENT)
    d1 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=pzaTOPICGENERAL1, client=CLIENT)
    
    logger.console("setting the pulling cycle")
    d.direction.polling_cycle.set(0.1)
    d.state.polling_cycle.set(0.1)
    d1.direction.polling_cycle.set(0.1)
    d1.state.polling_cycle.set(0.1)

@keyword("setting active state low ${CLIENT} ${GPIO} ${GPIO_IN}")
def settingActiveLow(CLIENT, GPIO, GPIO_IN):

    pzaTOPICGENERAL=f"pza/lab_paul/io_pza_controling/testing_of_io_controling{GPIO}"
    pzaTOPICGENERAL1=f"pza/lab_paul/io_pza_controling/testing_of_io_controling{GPIO_IN}"

    d = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=pzaTOPICGENERAL, client=CLIENT)
    d1 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=pzaTOPICGENERAL1, client=CLIENT)
    
    logger.console("setting the active state low")
    d.state.active_low.set(False)
    d1.state.active_low.set(False)


@keyword("writting to output and getting the input ${CLIENT} ${GPIO} ${GPIO_IN}")
def writtingOutput(CLIENT, GPIO, GPIO_IN):

    pzaTOPICGENERAL=f"pza/lab_paul/io_pza_controling/testing_of_io_controling{GPIO}"
    pzaTOPICGENERAL1=f"pza/lab_paul/io_pza_controling/testing_of_io_controling{GPIO_IN}"

    d = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=pzaTOPICGENERAL, client=CLIENT)
    d1 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=pzaTOPICGENERAL1, client=CLIENT)

    logger.console("setting writting the IO")
    d.state.active.set(True)
    time.sleep(1)
    result = d1.state.active.get()
    logger.console(result)
    time.sleep(1)
    d.state.active.set(False)
    time.sleep(1)
    result = d1.state.active.get()
    logger.console(result)