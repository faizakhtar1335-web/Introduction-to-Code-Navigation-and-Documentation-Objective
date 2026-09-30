"""
Week 1 - Code Navigation and Documentation
GitHub-ready beginner Python sample.

Run:
    python code_navigation_sample.py
"""

from dataclasses import dataclass


@dataclass
class Product:
    """Represent one product in the catalog."""
    product_id: int
    name: str
    price: float


def create_products():
    """Create and return the sample product catalog."""
    return [
        Product(1, "Keyboard", 1200.00),
        Product(2, "Mouse", 650.00),
        Product(3, "Headphones", 1800.00),
    ]


def display_products(products):
    """Display all products."""
    print("\nAvailable Products")
    print("-" * 35)

    for product in products:
        print(f"{product.product_id}. {product.name} - Rs.{product.price:.2f}")


def find_product(products, product_id):
    """Find a product by ID. Return None when it is not found."""
    for product in products:
        if product.product_id == product_id:
            return product
    return None


def calculate_total(cart):
    """Calculate the total price of products in the cart."""
    return sum(product.price for product in cart)


def checkout(cart):
    """Validate the cart and print the checkout result."""
    if not cart:
        print("\nCart is empty. Nothing to checkout.")
        return 0.0

    total = calculate_total(cart)
    print(f"\nCheckout successful. Total: Rs.{total:.2f}")
    return total


def main():
    """Run the sample code-navigation application."""
    products = create_products()
    cart = []

    display_products(products)

    selected_id = 2
    selected_product = find_product(products, selected_id)

    if selected_product is not None:
        cart.append(selected_product)
        print(f"\nAdded to cart: {selected_product.name}")
    else:
        print("\nProduct not found.")

    checkout(cart)


if __name__ == "__main__":
    main()
