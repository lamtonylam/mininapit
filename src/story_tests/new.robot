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
${booktitle}     kirjannimi

*** Test Cases ***
Submit and check for article citation
    GO TO  ${NEW_URL}
    Input Text  key_article  ${key}
    Input Text  author_article  ${author}
    Input Text  title_article  ${title}
    Input Text  journal_article  ${journal}
    Input Text  year_article  ${year}     
    Input Text  volume_article  ${volume}
    Input Text  pages_article  ${pages}
    Click Button  article
    Page Should Contain   mikko: tutkimus (lehti)

Submit inproceedings html form that isn't connected to anything
    GO TO  ${NEW_URL}
    Input Text  key_inproceedings  ${key}
    Input Text  author_inproceedings  ${author}
    Input Text  title_inproceedings  ${title}
    Input Text  year_inproceedings  ${year}    
    Input Text  booktitle_inproceedings  ${booktitle} 
    Click Button  inproceedings
