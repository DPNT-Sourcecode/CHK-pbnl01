from lib.solutions.CHK.checkout_solution import CheckoutSolution


class TestCheckout:
    def test_empty_string(self):
        assert CheckoutSolution().checkout(skus="") == -1

