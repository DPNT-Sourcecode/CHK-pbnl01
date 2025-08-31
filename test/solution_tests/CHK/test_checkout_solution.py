from lib.solutions.CHK.checkout_solution import CheckoutSolution


class TestHello:
    def test_craftsman(self):
        assert CheckoutSolution().checkout(skus="Craftsman") == "Hello, Craftsman!"
