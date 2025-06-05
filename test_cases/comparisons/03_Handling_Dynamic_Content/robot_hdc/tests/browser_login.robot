*** Settings ***
Resource    ../resources/keywords.robot
Resource    ../resources/variables.robot

*** Test Cases ***
Login With Chrome
    ${start_time}=    Get Time In Milliseconds
    Open Browser And Login    chrome
    Navigate To Photo Page
    ${initial_comments}=    Get Number Of Comments
    Log    Initial number of comments: ${initial_comments}
    Enter And Submit Comment
    ${updated_comments}=    Get Number Of Comments
    Log    Updated number of comments: ${updated_comments}
    Log Execution Time    ${start_time}
    Close Browser

