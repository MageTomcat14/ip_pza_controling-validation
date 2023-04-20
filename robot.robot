*** Settings ***
Library    pza.py
Library    String
Resource   test_env.resource
Library    Collections


*** Test Cases ***
# TestAddition
#     ${value}   SUM FUNCTION  ${2}  ${3}  # add the keywork of the function
#     Should Be Equal   ${value}  ${5}

# ConnectionToBrocker
#     ${value}   connect to client and MQTT
#     # Should Be True   ${value}
#     Log    ${value}

IO_1
    ${value}   connect to client and MQTT
    ${io1}   write LED 1 ${value}
    # Should Be True   ${value}
    Log    ${io1}

IO_2
    ${value}   connect to client and MQTT
    ${io2}   write LED 2 ${value}
    # ${value}   write LED 16
    # Should Be True   ${value}
    Log    ${value}

IO_16
    ${value}   connect to client and MQTT
    ${io16}   write LED 16 ${value}
    # ${value}   write LED 16
    # Should Be True   ${value}
    Log    ${io16}

IO_18
    ${value}   connect to client and MQTT
    ${io18}   write LED 18 ${value}
    # ${value}   write LED 16
    # Should Be True   ${value}
    Log    ${io18}
    # ${value}  write LED 18
    # # Should Be True   ${value}
    # Log    ${value}