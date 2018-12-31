def fiborabbits2(n, m):
    previewsvals = [1] + (m - 1) * [0]
    for i in range(2, n + 1):
        nextval = sum(previewsvals[1:])
        previewsvals = [nextval] + previewsvals[:-1]
    return sum(previewsvals)


print(fiborabbits2(87,18))