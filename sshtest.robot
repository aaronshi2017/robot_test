*** Settings ***
Library   class_moshellcommand.py

*** Variables ***


*** Test Cases ***
Test ls -al command
        ${result}=     class_moshellcommand.Commandexecution        ls -al
        Should Be Equal As Numbers   ${result}     0

Test cat /etc/os-release command
        ${result}=     class_moshellcommand.Commandexecution        cat /etc/os-release
        Should Be Equal As Numbers    ${result}     0

Test 
        ${value}=      class_moshellcommand.Ssh_close
        Should Be Equal As Integers    ${value}    0
