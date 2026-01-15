*** Test Cases ***
Pass Test
    Log    This test will pass
    Should Be Equal    1    1

Fail Test
    Log    This test will fail
    Should Be Equal    1    2



# To run the listener commans:
# robot --pythonpath Robot_Automation/Listeners --listener listener_basic.BasicListener Robot_Automation/Listeners/test.robot