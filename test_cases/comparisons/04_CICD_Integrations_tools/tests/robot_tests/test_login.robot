*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}             http://127.0.0.1:5000/auth/login
${USERNAME}        admin@helloflask.com
${PASSWORD}        helloflask

*** Test Cases ***
Login to Flask Application
    Open Browser    ${URL}    chrome
    Input Text    name=email    ${USERNAME}
    Input Text    name=password    ${PASSWORD}
    Click Button    name=submit
    Title Should Contain    Home - Albumy
    Close Browser
