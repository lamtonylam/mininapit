*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser

*** Variables ***
${key}     testi
${author}     mikko
${title}     tutkimus
${journal}     lehti
${year}     2000
${volume}     15
${pages}     20

*** Test Cases ***
Reset Tabke
    GO TO  ${RESET_URL}

Set article parameters
    GO TO  ${NEW_URL}
    Input Text  key  ${key}
    Input Text  author  ${author}
    Input Text  title  ${title}
    Input Text  journal  ${journal}
    Input Text  year  ${year}     
    Input Text  volume  ${volume}
    Input Text  pages  ${pages}

Submit citation
    Click Button  submit

Check for citation
    Page Should Contain   mikko: tutkimus (testi)