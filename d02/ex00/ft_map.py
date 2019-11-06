def ft_map(func, inputs):
    it = []
    for i in inputs:
        it = it + [func(i)]
    return it
