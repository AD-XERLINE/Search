def minweight(order, box):
    if box == 1:
        return sum(order)

    weight = 999999999999999999999999999999999999999999999999999999999999999
    for i in range(len(order)):

        if len(order[i:]) < box - 1:
            break

        this_box    =   sum(order[:i])
        other_box   =   minweight(order[i:], box - 1)
        weight  =   min(max(this_box, other_box), weight)
            
    return weight

txt = 'Minimum weigth for '
inp = input('Enter Input : ').split('/')
order, box = list(map(int, inp[0].split())), int(inp[1])
txt = txt + str(box) + ' box(es) = ' + str(minweight(order, int(box)))
print(txt)