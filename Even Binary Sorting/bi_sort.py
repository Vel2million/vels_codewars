from numpy import binary_repr

def binary_to_decimal(binary):
    return int(binary,2)


def is_even(decimal):
    return decimal % 2 == 0

    
def even_binary(n):
    binary_string = n.split(" ")
    binaries = []
    even_decimals = []

    for index, binary in enumerate(binary_string, 1):
        binaries.append({'index': index, 'binary': binary ,'decimal': binary_to_decimal(binary)})

    for index, bin_dict in enumerate(binaries):
        if is_even(bin_dict['decimal']):
            even_decimals.append(bin_dict['decimal'])
            binaries[index]['decimal'] = ''
            binaries[index]['binary'] = ''
    
    even_decimals = sorted(even_decimals)

    for dec in even_decimals:
        for bin_dict in binaries:
            if not bin_dict['decimal'] and not bin_dict['binary']:
                bin_dict['decimal'] = dec
                bin_dict['binary'] = binary_repr(dec, 3)
                break
    
    result = ""
    for bin_dict in binaries:
        result += bin_dict['binary'] + chr(32)

    return result.rstrip()

# NUMBER 1 SOLUTION
# 3 lines, FUCKING HOW???
def even_binary_winner(s):
    s = s.split()
    print(s)
    e = sorted(filter(lambda b: b[-1]=='0', s), reverse=True)
    print(e)
    return ' '.join(map(lambda b: e.pop() if b[-1]=='0' else b, s))

if __name__ == "__main__":
    binary = "101 111 100 001 010"
    # binary = "001 101 011 111 100"
    even_binary_winner(binary)