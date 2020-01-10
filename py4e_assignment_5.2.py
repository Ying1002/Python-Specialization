largest = None
smallest=None
while True:
    num = input ("Enter a number: ")
    if num=="done":
        break
    try:
        Int=int(num)
        if smallest is None:
            smallest=Int
        elif Int<smallest:
            smallest=Int
        if largest is None:
            largest=Int
        elif Int>largest:
            largest=Int
    except:
        print ("Invalid input")
        continue
print ("Maximum is",largest)
print ("Minimum is",smallest)
