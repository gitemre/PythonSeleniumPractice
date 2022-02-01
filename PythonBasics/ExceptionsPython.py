ItemsInCart = 0

if ItemsInCart != 2:
    pass

assert (ItemsInCart == 0)

try:
    with open('test.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print(e)

finally:
    print("cleaning up resources")
