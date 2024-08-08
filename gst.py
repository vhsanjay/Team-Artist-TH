def calculate_gst():
  price = float(input("Enter the price: "))
  gst_rate = float(input("Enter the GST rate (%): "))
  gst_amount = (price * gst_rate) / 100
  total_price = price + gst_amount
  print("GST Amount:", gst_amount)
  print("Total Price:", total_price)
calculate_gst()
