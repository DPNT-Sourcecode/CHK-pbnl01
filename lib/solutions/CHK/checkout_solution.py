class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):

        if skus is None:
            return -1
        if skus == "":
            return 0


