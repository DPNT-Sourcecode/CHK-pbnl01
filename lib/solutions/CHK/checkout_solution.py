from collections import Counter
from typing import Dict


class CheckoutSolution:

    PRICES: Dict[str, int] = {"A": 50, "B": 30, "C": 20, "D": 15}
    OFFERS: Dict[str, tuple[int, int]] = {"A": (3, 130), "B": (2, 45)}

    # skus = unicode string
    def checkout(self, skus):

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




