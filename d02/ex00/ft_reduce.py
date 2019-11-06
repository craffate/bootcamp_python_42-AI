def ft_reduce(func, inputs):
    for i in inputs:
        res = res + func(i)
    return res
