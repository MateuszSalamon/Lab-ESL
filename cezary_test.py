




while(True):
    out = 0
    print("insert key: ")
    key = int(input())
    # key = 2
    print("insert message: ")
    message = int(input())
    # message = 17
    state = 0
    maxval = 15


    if state == 1:
        out = message + key

        while ((out > maxval) or (out <=0)):
            if out > maxval:
                out = out - maxval

            elif out <= 0:
                out = out + maxval

    elif state == 0:
        out = message - key
        while ((out > maxval) or (out <= 0)):
            if out > maxval:
                out = out - maxval

            elif out <= 0:
                out = out + maxval
    else:
        print("no state set")

    print("OUT = ", out)