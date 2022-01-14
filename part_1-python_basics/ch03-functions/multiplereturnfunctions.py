def pastaprices(original,coupon):
    discounted = original - coupon
    markedup = coupon + original
    return discounted, markedup
discounted,markedup = pastaprices(90,10)

print("The pasta was marked up extra and it's price was was $" + str(markedup) + ", but with the coupon and the normal store price it was only $" + str(discounted) + ".")