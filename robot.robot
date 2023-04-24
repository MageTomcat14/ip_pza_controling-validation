* Settings ***
Library    pza.py
Library    String
Resource   test_env.resource
Library    Collections


*** Test Cases ***

ConnectionToBrocker
    ${CLIENT}   connect to client and MQTT
    Set Global Variable    ${CLIENT}
    Log    ${CLIENT}

# create the template to control IO    
IO_From_PICO
    [Tags]   OK
    [Template]  GPIO
    ${0}
    ${10}
    ${16}
    ${21}
    
# one test case for controling all IO's
*** Keywords ***
GPIO
    [Arguments]  ${GPIO_CONTROL}
    ${direction}  writting DIRECTION & STATE ${CLIENT} ${GPIO_CONTROL}
    Log  ${direction}
