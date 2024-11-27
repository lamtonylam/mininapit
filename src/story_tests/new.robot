*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       reset db

*** Variables ***
${key}     testi
${author}     mikko
${title}     tutkimus
${journal}     lehti
${year}     2000
${volume}     15
${pages}     20
${bibtex}    @article{testi,\n \ author = {mikko},\n \ title = {tutkimus},\n \ journal = {lehti},\n \ year = {2000},\n \ volume = {15},\n \ pages = {20}\n}

*** Test Cases ***
Submit and check for article citation
    GO TO  ${NEW_URL}
    Input Text  key  ${key}
    Input Text  author  ${author}
    Input Text  title  ${title}
    Input Text  journal  ${journal}
    Input Text  year  ${year}     
    Input Text  volume  ${volume}
    Input Text  pages  ${pages}
    Click Button  submit
    Page Should Contain   mikko: tutkimus (testi)

Submit and check that the toggle BibTeX button works
    GO TO  ${NEW_URL}
    Input Text  key  ${key}
    Input Text  author  ${author}
    Input Text  title  ${title}
    Input Text  journal  ${journal}
    Input Text  year  ${year}     
    Input Text  volume  ${volume}
    Input Text  pages  ${pages}
    Click Button  submit
    Page Should Contain   mikko: tutkimus (testi)
    Click Button  Toggle BibTeX
    Page Should Contain  ${bibtex}
    Click Button  Toggle normal citations
    Page Should Contain   mikko: tutkimus (testi)
