import numpy

def ft_mean(l: list):
    return sum(l) / len(l)


def ft_median(l: list):
    l.sort()
    n = len(l)
    middleIndex = n // 2
    if n % 2:
        return l[middleIndex]
    else:
        return (l[middleIndex - 1] + l[middleIndex]) / 2


def ft_quartiles(l: list):
    l.sort()
    i1 = len(l) // 4
    i3 = i1 * 3
    q1 = l[i1]
    q3 = l[i3]
    return [float(q1), float(q3)]


def ft_variance(l):
    mean = ft_mean(l)
    tot = sum((x - mean) ** 2 for x in l)
    n = len(l)
    variance = tot / n
    return(variance)


def ft_standard_deviation(l):
    variance = ft_variance(l)
    std = variance ** 0.5
    return(std)


def ft_statistics(*args: any, **kwargs: any) -> None:
    if not args:
        print("ERROR")
        print("ERROR")
        print("ERROR")
        return
    l = list(args)
    for key, value in kwargs.items():
        if value == 'mean':
            print(f'mean : {ft_mean(l)}')
        elif value == 'median':
            print(f'median : {ft_median(l)}')
        elif value == 'quartile':
            print(f'quartile : {ft_quartiles(l)}')
        elif value == 'std':
            print(f'std : {ft_standard_deviation(l)}')
        elif value == 'var':
            print(f'var : {ft_variance(l)}')
        else:
            return

