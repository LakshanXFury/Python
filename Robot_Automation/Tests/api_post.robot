*** Settings ***
Library     RequestsLibrary

*** Variables ***
${BASE_URL} =   https://jsonplaceholder.typicode.com
${ENDPONT} =    /posts

*** Test Cases ***
Create User Test
    ${headers} =     Create Dictionary       Content-Type=application/json
    ${body} =       Create Dictionary       name=Lakshan   job=Tester
    Create Session      mySession       ${BASE_URL}
    ${response}=    POST On Session     mySession   ${ENDPONT}     json=${body}    headers=${headers}
    Should Be Equal As Strings    ${response.status_code}    201
    Log     ${response.json()}

#What is Content-Type=application/json?
#It tells the server "I am sending you JSON data", so the server knows how to read your request body correctly.
#Without it, the server might not understand the body you're sending.