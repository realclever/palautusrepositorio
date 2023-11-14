*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  user  password1
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  password1
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  us  password1
    Output Should Contain  Username must be at least 3 characters long and only contain lower case characters

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  us1  password$
    Output Should Contain  Username must be at least 3 characters long and only contain lower case characters

Register With Valid Username And Too Short Password
    Input Credentials  user  passwor
    Output Should Contain  Password must be at least 8 characters long and must include a number, upper case or special character

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  user  password
    Output Should Contain  Password must be at least 8 characters long and must include a number, upper case or special character

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command