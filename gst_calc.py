# GST Calculator (Inclusive & Exclusive)

amount = float(input("Enter Amount: "))
gst = float(input("Enter GST Percentage: "))

print("\n1. Exclusive GST (Add GST)")
print("2. Inclusive GST (Remove GST)")

choice = int(input("Enter Your Choice (1/2): "))

if choice == 1:
    # Exclusive GST
    gst_amount = (amount * gst) / 100
    net_price = amount + gst_amount

    print("\n----- Exclusive GST -----")
    print("Original Cost :", amount)
    print("GST %         :", gst)
    print("GST Amount    :", gst_amount)
    print("Net Price     :", net_price)

elif choice == 2:
    # Inclusive GST
    original_cost = amount * (100 / (100 + gst))
    gst_amount = amount - original_cost

    print("\n----- Inclusive GST -----")
    print("Amount (Incl. GST):", amount)
    print("GST %             :", gst)
    print("Original Cost     :", round(original_cost, 2))
    print("GST Amount        :", round(gst_amount, 2))

else:
    print("Invalid Choice!")