*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    https://www.saucedemo.com/
${BROWSER}    Chrome

${USER}    standard_user
${PASSWORD}    secret_sauce

${element1}
${element2}
*** Test Cases ***
Sauce Demo
    Login    ${URL}    ${BROWSER}
    Reset the App State
    ${element1}    ${element2}=    Add 2 items
    Verify if the items in cart    ${element1}    ${element2}

*** Keywords ***
Login
    [Arguments]    ${URL}    ${BROWSER}
    open browser    ${URL}    ${BROWSER}
    maximize browser window
    wait until element is visible    //input[@placeholder="Username"]    5s
    input text    //input[@placeholder="Username"]    ${USER}
    input text    //input[@placeholder="Password"]    ${PASSWORD}
    click element    //input[@type="submit"]

Reset the App State
    ${INVENTORY_URL}=    get location
    LOG    ${INVENTORY_URL}
    click element    //button[text()="Open Menu"]
    wait until element is visible    //a[text()="Reset App State"]    5s
    click element    //a[text()="Reset App State"]
#    go to    ${INVENTORY_URL}

Add 2 items
    wait until element is visible    (//div[@class="inventory_item"]//button)[1]    5s
    click element    (//div[@class="inventory_item"]//button)[1]
    click element    (//div[@class="inventory_item"]//button)[2]
    ${element1}=    get text    (//div[@class="inventory_item"]//div[@class="inventory_item_label"]/a/div)[1]
    ${element2}=    get text    (//div[@class="inventory_item"]//div[@class="inventory_item_label"]/a/div)[2]
    log    ${element1}
    log    ${element2}

    RETURN    ${element1}    ${element2}

Verify if the items in cart
    [Arguments]    ${element1}    ${element2}
    wait until element is visible    //a[@class="shopping_cart_link"]
    click link    //a[@class="shopping_cart_link"]
    wait until element is visible    //div[@class="cart_item"]//a/div    5s
    ${extracted_element1}=    get text    (//div[@class="cart_item"]//a/div)[1]
    ${extracted_element2}=    get text    (//div[@class="cart_item"]//a/div)[2]

    should be equal    ${extracted_element1}    ${element1}
    should be equal    ${extracted_element2}    ${element2}


#✅ Option 1: Use a Dictionary
#You can return a dictionary from your Add 2 items keyword and access values by keys.
#
#✅ Modified Add 2 items Keyword:
#robot
#Copy
#Edit
#Add 2 items
#    wait until element is visible    (//div[@class="inventory_item"]//button)[1]    5s
#    click element    (//div[@class="inventory_item"]//button)[1]
#    click element    (//div[@class="inventory_item"]//button)[2]
#
#    ${item1}=    get text    (//div[@class="inventory_item"]//div[@class="inventory_item_label"]/a/div)[1]
#    ${item2}=    get text    (//div[@class="inventory_item"]//div[@class="inventory_item_label"]/a/div)[2]
#
#    &{items}=    Create Dictionary    item1=${item1}    item2=${item2}
#    [Return]    &{items}
#✅ Test Case Update:
#robot
#Copy
#Edit
#*** Test Cases ***
#Sauce Demo
#    Login    ${URL}    ${BROWSER}
#    Reset the App State
#    &{items}=    Add 2 items
#    Verify if the items in cart    ${items.item1}    ${items.item2}
#✅ Option 2: Use a List
#Add 2 items Keyword:
#robot
#Copy
#Edit
#Add 2 items
#    click element    (//div[@class="inventory_item"]//button)[1]
#    click element    (//div[@class="inventory_item"]//button)[2]
#
#    ${item1}=    get text    (//div[@class="inventory_item"]//div[@class="inventory_item_label"]/a/div)[1]
#    ${item2}=    get text    (//div[@class="inventory_item"]//div[@class="inventory_item_label"]/a/div)[2]
#
#    @{items}=    Create List    ${item1}    ${item2}
#    [Return]    @{items}
#Test Case:
#robot
#Copy
#Edit
#*** Test Cases ***
#Sauce Demo
#    Login    ${URL}    ${BROWSER}
#    Reset the App State
#    @{items}=    Add 2 items
#    Verify if the items in cart    ${items[0]}    ${items[1]}