def euklides_iter(a, b):
    while b:
        #pom = b
        #b = a % b
        #a = pom
        a, b = b, a % b
    return a


print(euklides_iter(24, 18))

