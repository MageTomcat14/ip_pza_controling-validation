* Settings ***
Library    testing.py
Library    String
Library    Collections

*** Test Cases ***

ConnectionToBrocker
    ${CLIENT}   connect to client and MQTT
    Set Global Variable    ${CLIENT}
    Log    ${CLIENT}

# create the template to control IO    
IO_From_PICO_SET
    [Tags]    OK
    [Template]    GPIO_SET 
    ${0}    ${1}   
    # ${2}    ${3}
    # ${4}    ${5}   
    # ${6}    ${7} 
    # ${8}    ${9}   
    # ${10}    ${11} 
    # ${12}    ${13}   
    # ${14}    ${15} 
    # ${16}    ${17}   
    # ${18}    ${19} 
    # ${20}    ${21}   
    # ${21}    ${22} 
    # ${26}    ${27}   
    # ${27}    ${28} 

# # one test case for controling all IO's
*** Keywords ***
GPIO_SET

    [Documentation]    Testing the inputs and outputs of the PICO
    [Tags]    OK        
    [Arguments]  ${GPIO_OUT}    ${GPIO_IN}
    ${INSTANCE_OUT}    ${INSTANCE_IN}    declaring topics and instances ${CLIENT} ${GPIO_OUT} ${GPIO_IN}


    # setting the direction of IO's
    setting IO ${GPIO_OUT} to output ${INSTANCE_OUT}
    setting IO ${GPIO_IN} to input ${INSTANCE_IN}


    setting pull of ${GPIO_IN} ${INSTANCE_IN}
    setting pulling cycle of IO ${GPIO_IN} and ${GPIO_OUT} ${INSTANCE_OUT} ${INSTANCE_IN}
    setting active state low ${INSTANCE_OUT} ${INSTANCE_IN}

    # write and read
    setting IO ${GPIO_OUT} to TRUE ${INSTANCE_OUT}
    getting the value of IO ${GPIO_IN} ${INSTANCE_IN}
    setting IO ${GPIO_OUT} to False ${INSTANCE_OUT}
    getting the value of IO ${GPIO_IN} ${INSTANCE_IN}


    # #simulating errors
    # configure pulls to a output ${GPIO_OUT} ${INSTANCE_OUT}
    # write to a input ${GPIO_IN} ${INSTANCE_IN}


*** Test Cases ***
END OF TESTS
    ending





















    # set the direction of the GPIO ${CLIENT} ${GPIO_OUT} ${GPIO_IN}
#     # set the pull direction of the GPIO ${CLIENT} ${GPIO_OUT} ${GPIO_IN}
#     # # set the pulling cycle direction of the GPIO ${CLIENT} ${GPIO_OUT} ${GPIO_IN}
#     # # set the active of state ${CLIENT} ${GPIO_OUT} ${GPIO_IN}
#     # # set the active low of state ${CLIENT} ${GPIO_OUT} ${GPIO_IN}
#     # # set the pulling cycle state ${CLIENT} ${GPIO_OUT} ${GPIO_IN}
    
    


    # Set Global Variable    ${d1}
    # getting DIRECTION & STATE of output ${CLIENT} ${GPIO_IN} ${d1}

# # one test case for controling all IO's
# *** Keywords ***
# GPIO_GET
#     [Arguments]  ${GPIO_OUT}    ${GPIO_IN}

    