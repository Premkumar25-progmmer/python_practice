fuels = {"1": ("Petrol", 110), "2": ("Diesel", 95)}

def show_fuels():
    print("\n===============================")
    print("     Available Fuel Types      ")
    print("===============================")
    for k, v in fuels.items():
        print(f"{k}. {v[0]:8s} → ₹{v[1]} per litre")
    print("===============================\n")

def calc_bill(ft, ltr):
    price = fuels[ft][1]
    sub = ltr * price
    disc = 200 if ltr > 50 else 0
    tot = sub - disc
    return sub, disc, tot

def receipt(ft, ltr, sub, disc, tot):
    print("\n=========== Fuel Receipt ===========")
    print(f"Fuel Type       : {fuels[ft][0]}")
    print(f"Litres Filled   : {ltr:.2f} L")
    print(f"Price per Litre : ₹{fuels[ft][1]}")
    print(f"Subtotal        : ₹{sub:.2f}")
    print(f"Discount Applied: ₹{disc}")
    print("------------------------------------")
    print(f"Total Payable   : ₹{tot:.2f}")
    print("====================================\n")

def pump():
    print("========== Petrol Pump Billing System ==========")
    more = 'y'
    while more == 'y':
        show_fuels()
        ft = input("Select fuel type (1/2): ").strip()
        if ft == "1" or ft == "2":
            try:
                ltr = float(input("Enter litres to fill: "))
                if ltr <= 0:
                    print("Invalid input.\n")
                elif ltr > 100:
                    print("Maximum 100 litres allowed.\n")
                else:
                    sub, disc, tot = calc_bill(ft, ltr)
                    receipt(ft, ltr, sub, disc, tot)
            except ValueError:
                print("Invalid input.\n")
        else:
            print("Invalid selection.\n")
        more = input("Another transaction? (y/n): ").strip().lower()
    print("\nThank you for visiting.")

if __name__ == "__main__":

    pump()
