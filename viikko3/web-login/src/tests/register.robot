*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  user
    Set Password  password1
    Set password_confirmation  password1
    Submit Register Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  us
    Set Password  password1
    Set password_confirmation  password1
    Submit Register Credentials
    Register Should Fail With Message  Username must be at least 3 characters long and only contain lower case characters

Register With Valid Username And Invalid Password
    Set Username  user
    Set Password  password
    Set password_confirmation  password
    Submit Register Credentials
    Register Should Fail With Message  Password must be at least 8 characters long and must include a number, upper case or special character

Register With Nonmatching Password And Password Confirmation
    Set Username  user
    Set Password  password1
    Set password_confirmation  password2
    Submit Register Credentials
    Register Should Fail With Message  Mismatched passwords

Login After Successful Registration
    Set Username  useri
    Set Password  password1
    Set password_confirmation  password1
    Submit Register Credentials
    Register Should Succeed
    Go To Login Page
    Login Page Should Be Open
    Set Username  useri
    Set Password  password1
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  use1
    Set Password  password1
    Set password_confirmation  password1
    Submit Register Credentials
    Register Should Fail With Message  Username must be at least 3 characters long and only contain lower case characters
    Go To Login Page
    Login Page Should Be Open
    Set Username  usei
    Set Password  password1
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password
    
*** Keywords ***

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}    

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}  

Submit Login Credentials
    Click Button  Login

Submit Register Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}
    
Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}