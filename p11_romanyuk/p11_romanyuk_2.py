# ВАШ КОД ТУТ
def rrange(begin, end, step = 1):
    if step == 0 :
        return []
    elif step > 0 and begin > end:
        return []
    elif step < 0 and begin < end:
        return []
    else:
        lst=[]
        if begin != end:
            lst.append(begin)
            lst.extend(rrange(begin+step, end, step))
        else:
            pass
        return lst
# ПЕРЕВІРКА

x = rrange(1, 10)
y = rrange(10, 1, -1)
z = rrange(10, 1, 1)
#print(x, y, z)

assert x == list(range(1, 10)), 'Failed test for simple range'
assert y == list(range(10, 1, -1)), 'Failed test for reverse range'
assert z == list(range(10, 1, 1)), 'Failed test for empty range'
print('All tests good!')