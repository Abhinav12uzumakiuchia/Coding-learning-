import turtle
juice = turtle. numinput("juice","number of juice glasses?")
tea = turtle. numinput("tea","number of tea cups?")
coffee = turtle. numinput("coffee","number of cups?")
cost_juice = 54
cost_tea = 26
cost_coffee = 50
bill = juice*cost_juice+tea*cost_tea+coffee*cost_coffee
gst = 0.18*bill
total_bill=bill+gst
print("amount rupees.",bill)
print("gst 018% rupees.",gst)
print("total amount with gst rupees.", total_bill)
