from collections import Counter
from math import remainder
from typing import Any, Dict


class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus) -> int:
        PRICES: Dict[str, int] = {
            "A": 50,
            "B": 30,
            "C": 20,
            "D": 15,
            "E": 40,
            "F": 10,
            "G": 20,
            "H": 10,
            "I": 35,
            "J": 60,
            "K": 70,
            "L": 90,
            "M": 15,
            "N": 40,
            "O": 10,
            "P": 50,
            "Q": 30,
            "R": 50,
            "S": 20,
            "T": 20,
            "U": 40,
            "V": 50,
            "W": 20,
            "X": 17,
            "Y": 20,
            "Z": 21,
        }
        OFFERS: Dict[str, list[tuple[int, int]]] = {
            "A": [(5, 200), (3, 130)],
            "B": [(2, 45)],
            "F": [(3, 20)],
            "H": [(10, 80), (5, 45)],
            "K": [(2, 150)],
            "P": [(5, 200)],
            "Q": [(3, 80)],
            "U": [(4, 120)],
            "V": [(3, 130), (2, 90)],
        }
        FREE_OFFERS: dict[str, dict[str, Any]] = {
            "E": {"item": "B", "qty": 2},
            "N": {"item": "M", "qty": 3},
            "R": {"item": "Q", "qty": 3},
        }

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

        for item, qty in chargable_items.items():
            if qty <= 0:
                continue

            if item in OFFERS:
                for bundle_size, bundle_price in OFFERS[item]:
                    bundles = qty // bundle_size
                    if bundles:
                        total += bundles * bundle_price
                        qty -= bundles * bundle_size
                if qty:
                    total += qty * PRICES[item]

            else:
                total += qty * PRICES[item]

        return total

