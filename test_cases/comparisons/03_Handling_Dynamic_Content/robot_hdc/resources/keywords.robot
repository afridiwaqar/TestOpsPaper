*** Settings ***
Library    SeleniumLibrary
Library    BuiltIn
Library    DateTime

*** Variables ***
${LOGIN_URL}     http://127.0.0.1:5000/auth/login
${PHOTO_URL}     http://127.0.0.1:5000/photo/34
${EMAIL}         admin@helloflask.com
${PASSWORD}      helloflask
${COMMENT}       This is a test comment.

*** Keywords ***
Open Browser And Login
    [Arguments]    ${browser}
    Open Browser    ${LOGIN_URL}    ${browser}
    Maximize Browser Window
    Input Text      name=email      ${EMAIL}
    Input Text      name=password   ${PASSWORD}
    Click Button    name=submit

Navigate To Photo Page
    Go To    ${PHOTO_URL}
    Wait Until Element Is Visible    css=div.comments    20s

Enter And Submit Comment
    Input Text    name=body    ${COMMENT}
    Click Button  name=submit
    Sleep    1s

Get Number Of Comments
    ${comments_text}=    Get Text    css=div.comments h3
    RETURN    ${comments_text}

Log Execution Time
    [Arguments]    ${start_time}
    ${end_time}=    Get Time In Milliseconds
    ${execution_time}=    Evaluate    (${end_time} - ${start_time}) / 1000
    Log    Execution Time: ${execution_time} seconds

Get Time In Milliseconds
    ${time_in_ms}=    Evaluate    time.time() * 1000    modules=time
    RETURN    ${time_in_ms}

