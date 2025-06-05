*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${LOGIN_URL}       http://127.0.0.1:5000/auth/login
${EMAIL}           admin@helloflask.com
${PASSWORD}        helloflask

*** Test Cases ***
Test Login Across Browsers
    FOR    ${BROWSER}    IN    @{BROWSERS}
        Run Keyword And Continue On Failure    Test Login    ${BROWSER}
    END

*** Keywords ***
Test Login
    [Arguments]    ${BROWSER}
    ${DRIVER_PATH}    Set Variable    ${BROWSER}_DRIVER_PATH
    ${EXECUTABLE_PATH}    Catenate    SEPARATOR=/    ${DRIVER_PATH}.replace('_DRIVER_PATH', '').replace('_', '/')
    Open Browser    ${LOGIN_URL}    ${BROWSER}    executable_path=${EXECUTABLE_PATH}
    Input Text    id=email    ${EMAIL}
    Input Text    id=password    ${PASSWORD}
    Press Key    id=password    \\13
    Wait Until Page Contains Element    xpath=//h1[@id='title']    timeout=10s
    Title Should Be    Home - Albumy
...    OR    Dashboard
    Log    ${BROWSER}: Login successful
    Close Browser

*** Variables ***
@{BROWSERS}    Chrome    Firefox    Edge
${CHROME_DRIVER_PATH}    /home/waqar/.wdm/drivers/chromedriver/linux64/125.0.6422.141/chromedriver-linux64/chromedriver
${FIREFOX_DRIVER_PATH}    /home/waqar/.wdm/drivers/geckodriver/linux64/v0.34.0/geckodriver
${EDGE_DRIVER_PATH}    /home/waqar/.wdm/drivers/edgedriver/linux64/125.0.2535.92/msedgedriver
${CHROME_OPTIONS}    {"headless":False}
${FIREFOX_OPTIONS}    {"headless":False}
${EDGE_OPTIONS}    {"headless":False}

