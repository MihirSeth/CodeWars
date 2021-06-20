def count_bits(n):
    bits = []
    while(n>0):
        dig=n%2
        bits.append(dig)
        n=n//2
        
    bits.reverse()

    calc= sum(bits)
    return calc

count_bits(1234)