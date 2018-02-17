def get_vat(price, vat_rate):
    try:
	    vat = float(price) / 100 * float(vat_rate)
	    price_no_vat = float(price) - vat
	    print(price_no_vat)
    except ValueError:
    	print ("Not a number")


price1 = "120be"
vat_rate1 = 18
get_vat(price1, vat_rate1)