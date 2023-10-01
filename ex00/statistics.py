def ft_mean(pop: list):
    return sum(pop) / len(pop)


def ft_median(pop: list):
    pop.sort()
    n = len(pop)
    middleIndex = n // 2
    if n % 2:
        return pop[middleIndex]
    else:
        return (pop[middleIndex - 1] + pop[middleIndex]) / 2


def ft_quartiles(pop: list):
    pop.sort()
    i1 = len(pop) // 4
    i3 = i1 * 3
    q1 = pop[i1]
    q3 = pop[i3]
    return [float(q1), float(q3)]


def ft_variance(pop):
    mean = ft_mean(pop)
    tot = sum((x - mean) ** 2 for x in pop)
    return (tot / len(pop))


def ft_standard_deviation(pop):
    return ft_variance(pop) ** 0.5


def ft_statistics(*args, **kwargs) -> None:
    if not args:
        for _ in range(3):
            print("ERROR")
        return

    pop = list(args)
    statistics_map = {
        'mean': ft_mean,
        'median': ft_median,
        'quartile': ft_quartiles,
        'std': ft_standard_deviation,
        'var': ft_variance
    }

    for _, value in kwargs.items():
        func = statistics_map.get(value)
        if func:
            print(f'{value} : {func(pop)}')
        else:
            return
