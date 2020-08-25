# naive, remove from cart and add to bag
# no consideration to different groupings

from collections import Counter, defaultdict

discounts = [0, 0, 0.05, 0.1, 0.2, 0.25]
book_price = 800

def total(basket: list) -> int:
    cart = Counter(basket)
    total = 0
    # strategy: remove different items from cart and sum
    while len(cart) > 0:
        discount_percentual = discounts[len(cart)]
        discount_value = book_price * discount_percentual
        total += len(cart) * (book_price - discount_value)
        cart.subtract({item: 1 for item in cart.keys()})
        cart += Counter() # remove zero and negative counts

    return total