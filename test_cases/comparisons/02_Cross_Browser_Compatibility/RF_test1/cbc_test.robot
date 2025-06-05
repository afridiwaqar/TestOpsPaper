*** Settings ***
Library           SeleniumLibrary

*** Variables ***
@{BROWSERS}        Edge    Chrome    Firefox
${URL}             http://127.0.0.1:5000/auth/login
${USERNAME}        admin@helloflask.com
${PASSWORD}        helloflask

*** Test Cases ***
Open Flask Application Login Page and Login
    FOR    ${browser}    IN    @{BROWSERS}
        ${start_time}=    Get Time
        Open Browser    ${URL}    ${browser}
        Maximize Browser Window

        Input Text    id=email    ${USERNAME}
        Input Password    id=password    ${PASSWORD}
        Click Button    id=submit

        # Optionally, you can add verifications or interactions on the home page here

        ${end_time}=    Get Time
        ${elapsed_time}=    Evaluate    (datetime.datetime.strptime('${end_time}', '%Y-%m-%d %H:%M:%S') - datetime.datetime.strptime('${start_time}', '%Y-%m-%d %H:%M:%S')).total_seconds()    modules=datetime
        Log    Browser ${browser}: ${elapsed_time} seconds

        Close Browser
    END
