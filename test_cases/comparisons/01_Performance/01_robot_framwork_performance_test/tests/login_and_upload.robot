*** Settings ***
Library    SeleniumLibrary
Library    Collections
Library    OperatingSystem
Library    String
Resource   ../resources/keywords.robot
Suite Setup    Setup Browser
Suite Teardown    Close Browser

*** Variables ***
${LOGIN_URL}       http://127.0.0.1:5000/auth/login
${UPLOAD_URL}      http://127.0.0.1:5000/upload
${EMAIL}           admin@helloflask.com
${PASSWORD}        helloflask
${IMAGE_PATH}      /home/waqar/FAST/TestOps/test_cases/playwrite/working_flawlessly/image.jpg


*** Test Cases ***
Login And Upload Image
    Open Browser To Login Page
    Fill Login Form
    Submit Login Form
    Wait Until Login Is Successful
    Navigate To Upload Page
    Upload Image
    Verify Upload Success

*** Keywords ***
Setup Browser
    Open Browser    ${LOGIN_URL}    chrome
    Maximize Browser Window

Open Browser To Login Page
    Go To    ${LOGIN_URL}

Fill Login Form
    Input Text    id=email    ${EMAIL}
    Input Text    id=password    ${PASSWORD}

Submit Login Form
    Click Button    id=submit

Wait Until Login Is Successful
    Wait Until Element Is Not Visible    id=email    timeout=15s

Navigate To Upload Page
    Go To    ${UPLOAD_URL}
    Wait Until Page Contains Element    css=form.dropzone    timeout=15s
    Capture Page Screenshot    name=navigate_to_upload_page.png

*** Settings ***
Library    OperatingSystem
Library    String

*** Variables ***
${IMAGE_PATH}      /home/waqar/FAST/TestOps/test_cases/playwrite/working_flawlessly/image.jpg

*** Keywords ***
Upload Image
    Log    Current URL: ${UPLOAD_URL}
    Log Elements    css=form.dropzone
    Capture Page Screenshot    name=before_upload_attempt.png

    # Ensure Dropzone is fully initialized and ready
    Wait Until Element Is Visible    css=form.dropzone    timeout=200s

    # Prepare the image content in base64
    ${image_content}=    Get Binary File    ${IMAGE_PATH}
    ${base64_encoded_content}=    Evaluate    base64.b64encode($image_content).decode('utf-8')    modules=base64

    # JavaScript code to add the file to Dropzone
    ${js_code}=    Set Variable    return Dropzone.forElement("form.dropzone").addFile(new File([window.atob('${base64_encoded_content}')], "uploaded_image.jpg", {type: "image/jpeg", lastModified: new Date().getTime()}));

    # Execute JavaScript
    Execute JavaScript    ${js_code}

    # Wait for the upload to complete (assuming it takes 3-4 seconds)
    Sleep    4s  # Adjust the time based on typical upload duration

    # Ensure the "Done" button is visible
    Wait Until Element Is Visible    css=.btn.btn-light.float-right    timeout=30s

    # Additional debugging
    Log    Attempting to click the Done button
    Capture Page Screenshot    name=before_clicking_done.png

    # Click the "Done" button using Click Element
    Click Element    css=.btn.btn-light.float-right

    Capture Page Screenshot    name=after_upload_attempt.png

Verify Upload Success
    Sleep    55s
    # Adjust the selector as necessary for your application
    Element Should Be Visible    css=.success-message-selector

Close Browser
    Close Browser

Log Elements
    [Arguments]    ${locator}
    ${elements}=    Get WebElements    ${locator}
    ${length}=    Get Length    ${elements}
    Log    Found ${length} elements with locator: ${locator}
    FOR    ${element}    IN    @{elements}
        ${tag}=    Get Element Attribute    ${element}    tagName
        ${id}=    Get Element Attribute    ${element}    id
        ${classes}=    Get Element Attribute    ${element}    class
        ${text}=    Get Text    ${element}
        Log    Element: <${tag} id=${id} class=${classes}> Text: ${text}
    END

