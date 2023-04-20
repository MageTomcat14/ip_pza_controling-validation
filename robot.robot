*** Settings ***
Library    pza.py
Library    String
Resource   test_env.resource
Library    Collections


*** Test Cases ***
# TestAddition
#     ${value}   SUM FUNCTION  ${2}  ${3}  # add the keywork of the function
#     Should Be Equal   ${value}  ${5}

ConnectionToBrocker
    ${value}   connect to client and MQTT
    # Should Be True   ${value}
    Log    ${value}

IO_1
    ${value}   write LED 1
    # Should Be True   ${value}
    Log    ${value}

IO_2
    ${value}   write LED 2
    # Should Be True   ${value}
    Log    ${value}

IO_16
    ${value}   write LED 16
    # Should Be True   ${value}
    Log    ${value}

IO_18
    ${value}  write LED 18
    # Should Be True   ${value}
    Log    ${value}