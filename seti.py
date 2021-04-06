def decimal_to_binary(decimal_number):
    """Returns the array of digits in binary representation of a decimal number"""
    
    list = []
    while decimal_number > 0:
        elem = decimal_number % 2
        list.insert(0, elem)
        decimal_number //= 2
    return list

print(decimal_to_binary(24))


def binary_to_decimal(binary_digits): 
    """Returns the decimal (number) representation of a binary number represented by an array of 0/1 digits"""
    decimal, i, n = 0, 0, 0
    binary_digits = int("".join(str(x) for x in binary_digits))
    while (binary_digits != 0):
        dec = binary_digits % 10
        decimal = decimal + dec * pow(2, i) # (2 ** i)
        binary_digits = binary_digits // 10
        i += 1
    print(decimal)
    # nem működik úgy, ahogy a feladatban volt az input, azaz ilyen formátumú inputnál
binary_to_decimal([1, 0, 1, 0, 0])

    
def dec_to_base(num,base):  #Maximum base - 36
    """Returns the digits in destination_base representation of the decimal number"""
    base_num = []
    base_num = [int(i) for i in base_num]
    while num>0:
        dig = int(num%base)
        if dig<10:
            base_num += [int(i) for i in str(dig)]
        else:
            base_num += chr(ord('A')+dig-10)  #Using uppercase letters
        num //= base
    base_num = base_num [::-1]  #To reverse the string
    return base_num

print(dec_to_base(20, 8))


def base_to_decimal(digits, original_base):
    """Returns the decimal (number) representation of an array of digits given in original_base"""
    pass


def digits_as_string(digits, base):
    """Returns the string representation of an array of digits given in base"""
    pass


def convert_base(original_digits, original_base, destination_base):
    """Conversion from any base to any other base"""
    pass
