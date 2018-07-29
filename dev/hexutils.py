__hex_letters= {"a":10,
        "b":11,
        "c":12,
        "d":13,
        "e":14,
        "f":15}

def intohex(number, hex_prefix=False, uppercase=False):
    if type(number) is not int:
        raise TypeError("Value to convert must be int")
    def hexdivide(target):
        if target%16 > 9:
            for item in __hex_letters:
                if __hex_letters[item] == (target%16):
                    if uppercase:
                        return(item.upper())
                    else:
                        return(item)
            return(target%16)
        return(target%16)

    values = []
    while (number//16) is not 0:
        values.insert(0, hexdivide(number))
        number = number//16
    values.insert(0, hexdivide(number))
    if hex_prefix:
        return("0x" + ("".join(str(item) for item in values)))
    else:
        return("".join(str(item) for item in values))


def hextoint(target):
    if type(target) is not str:
        raise TypeError ("Argument must be str")
    decimals = []
    if target[:2] is "0x":
        target = target[2:]
    power_of_sixteen = len(target)-1
    for item in target:
        try:
            decimals.append(int(item)*(16**power_of_sixteen))
        except:
            if item.lower() in __hex_letters:
                decimals.append(__hex_letters[item.lower()]*(16**power_of_sixteen))
            else:
                raise ValueError (item, "doesn't belong to hex system")

        power_of_sixteen -= 1
    else:
        return(sum(decimals))


def hex_add(first, second, hex_output, hex_output_prefix=False, hex_output_upper=False):
    if (type(first) is not str) or (type(second) is not str):
        raise TypeError ("Addend type must be str. Use intohex(int value)")
    result = hextoint(first) + hextoint(second)
    if hex_output:
        return(intohex(result, hex_output_prefix, hex_output_upper))
    else:
        return(result)


def hex_subtract(first, second, hex_output, hex_output_prefix=False, hex_output_upper=False):
    if (type(first) is not str) or (type(second) is not str):
        raise TypeError ("Addend type must be str. Use intohex(int value)")
    result = hextoint(first) - hextoint(second)
    if hex_output:
        return(intohex(result, hex_output_prefix, hex_output_upper))
    else:
        return(result)


def hex_multiply(first, second, hex_output, hex_output_prefix=False, hex_output_upper=False):
    if (type(first) is not str) or (type(second) is not str):
        raise TypeError ("Addend type must be str. Use intohex(int value)")
    result = hextoint(first) * hextoint(second)
    if hex_output:
        return(intohex(result, hex_output_prefix, hex_output_upper))
    else:
        return(result)

def hex_divide(first, second, hex_output, hex_output_prefix=False, hex_output_upper=False):
    if (type(first) is not str) or (type(second) is not str):
        raise TypeError ("Addend type must be str. Use intohex(int value)")
    result = hextoint(first) // hextoint(second)
    if hex_output:
        return(intohex(result, hex_output_prefix, hex_output_upper))
    else:
        return(result)


def hex_floor(first, second, hex_output, hex_output_prefix=False, hex_output_upper=False):
    if (type(first) is not str) or (type(second) is not str):
        raise TypeError ("Addend type must be str. Use intohex(int value)")
    result = hextoint(first) % hextoint(second)
    if hex_output:
        return(intohex(result, hex_output_prefix, hex_output_upper))
    else:
        return(result)
