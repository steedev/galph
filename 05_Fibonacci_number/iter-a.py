def fibbo(n):
    f0 = 0
    f1 = 1
    fi = 0
    if n == 1:
        return 1
    for i in range(0, n-1):
        fi = f0 + f1
        f0 = f1
        f1 = fi
    return fi


print(fibbo(10))

