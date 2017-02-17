for a in [[1, 2, 3], [4, 5, 6], [7, 8, 9]]:
    if a != 0:
        print('-' * 20)
        for b in range(2, 10):
            print('{}x{}={}'.format(a[0], b, a[0] * b),
                  '{}x{}={}'.format(a[1], b, a[0] * b),
                  '{}x{}={}'.format(a[2], b, a[0] * b))
