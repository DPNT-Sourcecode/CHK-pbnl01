from lib.solutions.CHK.checkout_solution import CheckoutSolution


class TestCheckout:
    def test_none(self):
        assert CheckoutSolution().checkout(skus=None) == -1

    def test_empty_string(self):
        assert CheckoutSolution().checkout(skus="") == 0

    def test_invalid_type(self):
        assert CheckoutSolution().checkout(skus=1) == -1

    def test_invalid_skus(self):
        assert CheckoutSolution().checkout(skus="abcd") == -1
        assert CheckoutSolution().checkout(skus="a-bAB") == -1

    def test_valid_skus(self):
        assert CheckoutSolution().checkout(skus="A") == 50
        assert CheckoutSolution().checkout(skus="AB") == 80
        assert CheckoutSolution().checkout(skus="CDBA") == 115
        assert CheckoutSolution().checkout(skus="AA") == 100
        assert CheckoutSolution().checkout(skus="AAA") == 130
        assert CheckoutSolution().checkout(skus="AAAA") == 180
        assert CheckoutSolution().checkout(skus="AAAAA") == 200
        assert CheckoutSolution().checkout(skus="AAAAAA") == 250
        assert CheckoutSolution().checkout(skus="E") == 40
        assert CheckoutSolution().checkout(skus="EE") == 80
        assert CheckoutSolution().checkout(skus="EEEEE") == 200
        assert CheckoutSolution().checkout(skus="EEB") == 80
        assert CheckoutSolution().checkout(skus="FFF") == 20
        assert CheckoutSolution().checkout(skus="ABDFEFFAA") == 235
        assert CheckoutSolution().checkout(skus="AAABBDFEFFAA") == 320
        assert CheckoutSolution().checkout(skus="RRRQQQ") == 210  # 3 * 50 + 2 * 30
