*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       reset db

*** Test Cases ***
When navigating to main, the page loads and shows an empty listing
    go to                ${HOME_URL}
    title should be      Bibtex-apuri
    page should contain  Ei lisättyjä viitteitä
