# main.py
from products import Product
from store import Store


def show_menu():
    """Display the main menu options."""
    print("\nWelcome to the Store!")
    print("1. List all products")
    print("2. Show total stock quantity")
    print("3. Make an order")
    print("4. Quit")


def handle_list_products(store: Store):
    """Show all available products."""
    print("\nAvailable products:")
    for p in store.get_all_products():
        p.show()


def handle_total_quantity(store: Store):
    """Show the total quantity of items in the store."""
    print(f"\nTotal quantity in store: {store.get_total_quantity()}")


def handle_order(store: Store):
    """
    Ask the user for multiple product orders until 'done' is entered,
    then process the order and display total cost after confirmation.
    """
    shopping_list = []
    while True:
        product_name = input("\nEnter product name (or 'done' to finish): ").strip()
        if product_name.lower() == "done":
            break

        product = next((p for p in store.get_all_products() if p.name.lower() == product_name.lower()), None)
        if not product:
            print("Product not found.")
            continue

        try:
            qty = int(input(f"Enter quantity of '{product.name}': "))
            if qty <= 0:
                print("Quantity must be positive.")
                continue
            shopping_list.append((product, qty))
        except ValueError:
            print("Invalid quantity. Please enter a number.")

    if not shopping_list:
        print("No items ordered.")
        return

    # Show shopping list for confirmation
    print("\nYour shopping list:")
    for product, qty in shopping_list:
        print(f"{product.name} x {qty} = ${product.price * qty:.2f}")

    confirm = input("Confirm order? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("Order cancelled.")
        return

    # Process the order
    try:
        total_cost = store.order(shopping_list)
        print(f"\nOrder processed. Total cost: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Order failed: {e}")


def start(store: Store):
    """Starts the user interface for interacting with the store."""
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            handle_list_products(store)
        elif choice == "2":
            handle_total_quantity(store)
        elif choice == "3":
            handle_order(store)
        elif choice == "4":
            print("Thank you for visiting!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


def main():
    """Main entry point: create store and start program."""
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250)
    ]
    store = Store(product_list)
    start(store)


if __name__ == "__main__":
    main()
