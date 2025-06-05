*** Settings ***
Library    SeleniumLibrary
Library    pyautogui
Library    String
Library    ./pyautogui_library.py
Resource    /home/waqar/FAST/TestOps/test_cases/comparisons/03_Handling_Dynamic_Content/robot_hdc/resources/keywords.robot
Resource    /home/waqar/FAST/TestOps/test_cases/comparisons/03_Handling_Dynamic_Content/robot_hdc/resources/variables.robot

*** Variables ***
${LOGIN_URL}    http://127.0.0.1:5000/auth/login
${UPLOAD_URL}    http://127.0.0.1:5000/upload
${EMAIL}    admin@helloflask.com
${PASSWORD}    helloflask
${FILE_PATHS}    /home/waqar/FAST/papers/Image_1.jpg:/home/waqar/FAST/papers/Image_2.jpg:/home/waqar/FAST/papers/Image_3.jpg:/home/waqar/FAST/papers/Image_4.jpg:/home/waqar/FAST/papers/Image_5.jpg:/home/waqar/FAST/papers/Image_6.jpg:/home/waqar/FAST/papers/Image_7.jpg:/home/waqar/FAST/papers/Image_8.jpg:/home/waqar/FAST/papers/Image_9.jpg:/home/waqar/FAST/papers/Image_10.jpg:/home/waqar/FAST/papers/Image_11.jpg:/home/waqar/FAST/papers/Image_12.jpg:/home/waqar/FAST/papers/Image_13.jpg:/home/waqar/FAST/papers/Image_14.jpg:/home/waqar/FAST/papers/Image_15.jpg:/home/waqar/FAST/papers/Image_16.jpg:/home/waqar/FAST/papers/Image_17.jpg:/home/waqar/FAST/papers/Image_18.jpg:/home/waqar/FAST/papers/Image_19.jpg:/home/waqar/FAST/papers/Image_20.jpg:/home/waqar/FAST/papers/Image_21.jpg:/home/waqar/FAST/papers/Image_22.jpg:/home/waqar/FAST/papers/Image_23.jpg:/home/waqar/FAST/papers/Image_24.jpg:/home/waqar/FAST/papers/Image_25.jpg:/home/waqar/FAST/papers/Image_26.jpg:/home/waqar/FAST/papers/Image_27.jpg:/home/waqar/FAST/papers/Image_28.jpg:/home/waqar/FAST/papers/Image_29.jpg:/home/waqar/FAST/papers/Image_30.jpg:/home/waqar/FAST/papers/Image_31.jpg:/home/waqar/FAST/papers/Image_32.jpg:/home/waqar/FAST/papers/Image_33.jpg:/home/waqar/FAST/papers/Image_34.jpg:/home/waqar/FAST/papers/Image_35.jpg:/home/waqar/FAST/papers/Image_36.jpg:/home/waqar/FAST/papers/Image_37.jpg:/home/waqar/FAST/papers/Image_38.jpg:/home/waqar/FAST/papers/Image_39.jpg:/home/waqar/FAST/papers/Image_40.jpg:/home/waqar/FAST/papers/Image_41.jpg:/home/waqar/FAST/papers/Image_42.jpg:/home/waqar/FAST/papers/Image_43.jpg:/home/waqar/FAST/papers/Image_44.jpg:/home/waqar/FAST/papers/Image_45.jpg:/home/waqar/FAST/papers/Image_46.jpg:/home/waqar/FAST/papers/Image_47.jpg:/home/waqar/FAST/papers/Image_48.jpg:/home/waqar/FAST/papers/Image_49.jpg:/home/waqar/FAST/papers/Image_50.jpg:/home/waqar/FAST/papers/Image_51.jpg:/home/waqar/FAST/papers/Image_52.jpg:/home/waqar/FAST/papers/Image_53.jpg:/home/waqar/FAST/papers/Image_54.jpg:/home/waqar/FAST/papers/Image_55.jpg:/home/waqar/FAST/papers/Image_56.jpg:/home/waqar/FAST/papers/Image_57.jpg:/home/waqar/FAST/papers/Image_58.jpg:/home/waqar/FAST/papers/Image_59.jpg:/home/waqar/FAST/papers/Image_60.jpg:/home/waqar/FAST/papers/Image_61.jpg:/home/waqar/FAST/papers/Image_62.jpg:/home/waqar/FAST/papers/Image_63.jpg:/home/waqar/FAST/papers/Image_64.jpg:/home/waqar/FAST/papers/Image_65.jpg:/home/waqar/FAST/papers/Image_66.jpg:/home/waqar/FAST/papers/Image_67.jpg:/home/waqar/FAST/papers/Image_68.jpg:/home/waqar/FAST/papers/Image_69.jpg:/home/waqar/FAST/papers/Image_70.jpg:/home/waqar/FAST/papers/Image_71.jpg:/home/waqar/FAST/papers/Image_72.jpg:/home/waqar/FAST/papers/Image_73.jpg:/home/waqar/FAST/papers/Image_74.jpg:/home/waqar/FAST/papers/Image_75.jpg:/home/waqar/FAST/papers/Image_76.jpg:/home/waqar/FAST/papers/Image_77.jpg:/home/waqar/FAST/papers/Image_78.jpg:/home/waqar/FAST/papers/Image_79.jpg:/home/waqar/FAST/papers/Image_80.jpg:/home/waqar/FAST/papers/Image_81.jpg:/home/waqar/FAST/papers/Image_82.jpg:/home/waqar/FAST/papers/Image_83.jpg:/home/waqar/FAST/papers/Image_84.jpg:/home/waqar/FAST/papers/Image_85.jpg:/home/waqar/FAST/papers/Image_86.jpg:/home/waqar/FAST/papers/Image_87.jpg:/home/waqar/FAST/papers/Image_88.jpg:/home/waqar/FAST/papers/Image_89.jpg:/home/waqar/FAST/papers/Image_90.jpg:/home/waqar/FAST/papers/Image_91.jpg:/home/waqar/FAST/papers/Image_92.jpg:/home/waqar/FAST/papers/Image_93.jpg:/home/waqar/FAST/papers/Image_94.jpg:/home/waqar/FAST/papers/Image_95.jpg:/home/waqar/FAST/papers/Image_96.jpg:/home/waqar/FAST/papers/Image_97.jpg:/home/waqar/FAST/papers/Image_98.jpg:/home/waqar/FAST/papers/Image_99.jpg:/home/waqar/FAST/papers/Image_100.jpg

*** Test Cases ***
Upload Files
    ${start_time}=    Get Time In Milliseconds
    Open Browser    ${LOGIN_URL}    chrome
    Maximize Browser Window
    Input Text    id=email    ${EMAIL}
    Input Text    id=password    ${PASSWORD}
    Click Element    id=submit
    Wait Until Element Is Not Visible    id=email
    ${file_paths}    Split String    ${FILE_PATHS}    :
    FOR    ${file_path}    IN    @{file_paths}
        Go To    ${UPLOAD_URL}
        Wait Until Element Is Visible    id=myDropzone    timeout=10s
        Click Element    id=myDropzone
        BuiltIn.Sleep    1
        PyAutoGUI.Typewrite    ${file_path}    # use the custom keyword
        PyAutoGUI.Press    enter    # use the custom keyword
        BuiltIn.Sleep    1
        Click Link    Done
        BuiltIn.Sleep    1
    END
    Log Execution Time    ${start_time}
    Close Browser
