
def listFunc(a, b):
    return [i for i in range(a, b+1)]  # Create list of ints from a to b, Haskell equivalent [a..b]

def applicatorFunc(inpFunc, s, a, b):
    if s == 's':
        return sum(inpFunc(a, b))
    else:
        return sum(inpFunc(a, b)) / (b - a + 1)

print(applicatorFunc(listFunc, 'a', 1, 10))
