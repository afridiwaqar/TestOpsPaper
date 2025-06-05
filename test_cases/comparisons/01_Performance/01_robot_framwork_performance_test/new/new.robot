*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BROWSER}    Chrome
${URL}        http://127.0.0.1:5000
${LOGIN_URL}       http://127.0.0.1:5000/auth/login

*** Test Cases ***
Upload Image to Flask Albumy
    Open Browser    ${LOGIN_URL}    ${BROWSER}
    Wait Until Page Contains Element    id=email
    Input Text    id=email    admin@helloflask.com
    Input Text    id=password    helloflask
    Click Button    id=submit
    Wait Until Element Is Not Visible    id=email
    ${csrf_token}=    Get Element Attribute    id=csrf_token    value
    Go To    ${URL}/upload
    Wait Until Page Contains    Choose File
    Choose File    css=input[type="file"]    /home/waqar/FAST/TestOps/test_cases/playwrite/working_flawlessly/image.jpg
    Click Button    css=.btn.btn-light.float-right
    Sleep    5s
    Close Browser

