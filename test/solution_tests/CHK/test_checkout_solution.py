from lib.solutions.CHK.checkout_solution import CheckoutSolution


class TestCheckout:
    def test_none(self):
        assert CheckoutSolution().checkout(skus=None) == -1

    def test_empty_string(self):
        assert CheckoutSolution().checkout(skus="") == 0

    def test_invalid_type(self):
        assert CheckoutSolution().checkout(skus=1) == -1



