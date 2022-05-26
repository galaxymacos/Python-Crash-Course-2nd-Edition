def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"making a {size}-inch pizza with the following topping")
    for topping in toppings:
        print(f"- {topping}")