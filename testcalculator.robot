*** Settings ***
Variables     calculator.py

*** Test Cases ***
Test Addition
    ${result}=     Call Method    ${cal}    add     20    50
    Should Be Equal As Integers        ${result}       70

Test Addition2
    ${result}=     Call Method    ${cal}  add     80    90
    Should Be Equal As Numbers        ${result}        170