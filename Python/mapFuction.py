def mapTo(val, in1, in2, out1, out2):
    baseInput = (in2-in1)/100
    baseOutput = (out2-out1)/100

    maped = val/baseInput
    maped = baseOutput*maped

    return maped

if __name__ == "__main__":
    print(mapTo(30, 10,100, 20, 200))
