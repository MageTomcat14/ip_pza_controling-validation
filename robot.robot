*** Settings ***
Library    pza.py
Library    String
Resource   test_env.resource
Library    Collections


*** Test Cases ***

ConnectionToBrocker
    ${CLIENT}   connect to client and MQTT
    Set Global Variable    ${CLIENT}
    Log    ${CLIENT}

IO_1
    ${io1}   write LED 1 ${CLIENT}
    Log    ${io1}

IO_2
    ${io2}   write LED 2 ${CLIENT}
    Log    ${io2}
    # ${value}   write LED 16
    # Should Be True   ${value}

IO_16
    ${io16}   write LED 16 ${CLIENT}
    Log    ${io16}
    # ${value}   write LED 16
    # Should Be True   ${value}

IO_18
    ${io18}   write LED 18 ${CLIENT}
    Log    ${io18}
    # ${value}  write LED 18
    # Log    ${value}
