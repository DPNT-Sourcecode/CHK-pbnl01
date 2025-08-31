from collections import Counter
from math import remainder
from typing import Any, Dict


class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        PRICES: Dict[str, int] = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}
        OFFERS: Dict[str, list[tuple[int, int]]] = {
            "A": [(5, 200), (3, 130)],
            "B": [(2, 45)],
        }
        FREE_OFFERS: dict[str, dict[str, Any]] = {"E": {"item": "B", "qty": 2}}

        if not isinstance(skus, str):
            return -1
        if skus is None:
            return -1
        if skus == "":
            return 0

        counts: Counter[str] = Counter(skus)

        if any(char not in PRICES for char in skus):
            return -1

        chargable_items = counts.copy()
        for item, rule in FREE_OFFERS.items():
            if item in counts:
                free_item = rule["item"]
                free_qty = rule["qty"]
                free_items = counts[item] // free_qty
                if free_items and free_item in chargable_items:
                    chargable_items[free_item] = max(
                        0, chargable_items[free_item] - free_items
                    )

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


