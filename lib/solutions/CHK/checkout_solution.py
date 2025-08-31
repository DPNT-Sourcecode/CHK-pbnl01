from collections import Counter
from math import remainder
from typing import Dict


class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        PRICES: Dict[str, int] = {"A": 50, "B": 30, "C": 20, "D": 15}
        OFFERS: Dict[str, tuple[int, int]] = {"A": (3, 130), "B": (2, 45)}

        if not isinstance(skus, str):
            return -1
        if skus is None:
            return -1
        if skus == "":
            return 0

        counts: Counter[str] = Counter(skus)
        total: int = 0

        for item, qty in counts.items():
            price = PRICES[item]
            if item in OFFERS:
                bundle_size, bundle_price = OFFERS[item]
                bundles = qty // bundle_size
                remainder = qty % bundle_size
                total += bundles * bundle_price + remainder * price
            else:
                total += qty * price

        return total





