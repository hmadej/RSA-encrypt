
e = (2**80) + 1
n = 172832441894998260376220012196504623107426809480060512025867051243862591841142762389754856720075168799498705818668742751
block_size = len(str(n))//3
if (block_size * 3 < len(str(n))):
    block_size += 1


text = "One morning, when Gregor Samsa woke from troubled dreams, he found himself transformed in his bed in"


def str_to_num(string):
    padding = 32
    pt = string
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
