from lib.solutions.HLO.hello_solution import HelloSolution


class TestHello:
    def test_craftsman(self):
        assert HelloSolution().hello(friend_name="Craftsman") == "Hello, World!"

    def test_mr_x(self):
        assert HelloSolution().hello(friend_name="Mr. X") == "Hello, World!"

    def test_empty_string(self):
        assert HelloSolution().hello(friend_name="") == "Hello, World!"



