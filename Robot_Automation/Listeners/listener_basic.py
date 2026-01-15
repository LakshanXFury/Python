class BasicListener:
    ROBOT_LISTENER_API_VERSION = 2

    def start_test(self, name, attributes):
        print(f"\n>>> Starting test: {name}")

    def end_test(self, name, attributes):
        status = attributes['status']
        print(f">>> Test '{name}' ended with status: {status}")

        if status == 'FAIL':
            print(f">>> Failure message: {attributes['message']}")

"""
When you register a listener with --listener, Robot Framework:

Imports your listener class
Creates an instance of it
Checks what methods exist in your class
Automatically calls those methods at the right time with the right parameters
"""