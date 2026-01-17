To RuN Tags

# Run only smoke tests
robot --include smoke test_suite.robot

# Run multiple tag combinations
robot --include smoke --include critical test_suite.robot

# Exclude specific tags
robot --exclude destructive test_suite.robot
--------------------------------------------------------------

To Run Test

# Run single test
robot --test "Login Test" test.robot

# Run multiple specific tests
robot --test "Login Test" --test "Logout Test" test.robot

--------------------------------------------------------------

To Run Suite

# Run specific suite
robot --suite "Login Suite" test_directory/

# Run multiple suites
robot --suite "Login Suite" --suite "User Suite" test_directory/


