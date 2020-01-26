head = input('Head: ')
with open('head.csv', 'w') as file:
    lh = head.split('_')
    for i in range(len(lh)):
        lh[i] = lh[i][:1].upper() + lh[i][1:]
    head = ''.join(lh)
    file.write(head)