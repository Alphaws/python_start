def print_product(product):
    print(f"{product[0]} - {product[1]} db - {product[2]} Ft/db")

def main():
    # Üdvözöl, kiírja a program címét
    print("Bevásárló lista program. Kilépés q-val.")
    my_cart = [("alma", 5, 120), ("körte", 3, 150), ("szilva", 2, 200)]
    while True:
        print("\nAktuális lista:")
        print(my_cart)
        product_name = input(f"\nTermék neve: ")
        if product_name == "":
            break
        if product_name == "q":
            print("Szia!")
            break
        product_qty = int(input("Mennyiség: "))
        product_price = int(input("Ár (Ft / db): "))
        my_cart.append((product_name, product_qty, product_price))
        print(my_cart)

        print(f"\nA bevásárló lista {len(my_cart)} terméket tartalmaz.")
        print(f"\nA bevásárló lista összege: {sum(product[1] * product[2] for product in my_cart)} Ft")
        # Kiírja az első 3 elemet
        print(f"\nAz első 3 elem: {my_cart[:3]}")
        # Kiírja az elemeket a 3. elemtől
        print(f"\nAz elemek a 3. elemtől: {my_cart[2:]}")
        #Kiírja az utolsó 2 elemet
        print(f"\nAz utolsó 2 elem: {my_cart[-2:]}")

if __name__ == '__main__':
    main()
