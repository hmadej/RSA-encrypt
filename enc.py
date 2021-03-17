
e = (2**80) + 1
n = 3855338695276690252908107137430493656065677413967434998013726871721184398596748175116146312869263538623

text = "One morning, when Gregor Samsa woke from troubled dreams, he found how"


def str_to_num(string):
    padding = 32
    pt = string
    block_size = len(str(n))//3 + 1
    if len(pt) >= block_size:
        strings = [(pt[i:i+(block_size - 1)]) for i in range(0, len(pt), (block_size - 1))]
        
        strings[-1] = strings[-1] + chr(padding)*(block_size - (1 + len(strings[-1])))
        
        return [sum([ord(txt[len(txt) - (i+1)])*(1000**i) for i in range(len(txt))]) for txt in strings]
    else:
        txt = pt + chr(padding)*(block_size - (1 + len(pt)))
        return [sum([ord(txt[len(txt)-(i+1)]) *(1000**i) for i in range(len(txt))])]



def num_to_str(num):
    num_str = str(num)
    l = len(num_str)
    return "".join([chr(int(num_str[i:i+3])) for i in range(0, l, 3)])


def rsa_ende_crypt(inp, key):
    print(inp)
    e, n = key
    def fast(base):
        prev = base
        for bit in bin(e)[3:]:
            if bit == '1':
                prev = ((prev**2)*base) % n
            else:
                prev = (prev**2) % n
        return prev
    return fast(inp)


print(" # ".join([str(rsa_ende_crypt(number, (e,n))) for number in str_to_num(text)]))