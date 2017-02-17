for a in [[1, 2, 3], [4, 5, 6], [7, 8, 9]]:
        print('-' * 20)
        for b in range(1, 10):
            print('{}x{}={}\t'.format(a[0], b, a[0] * b),
                  '{}x{}={}\t'.format(a[1], b, a[0] * b),
                  '{}x{}={}\t'.format(a[2], b, a[0] * b))
