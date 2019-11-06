def ft_filter(func, inputs):
    it = []
    for i in inputs:
        if func(i):
            it = it + [func(i)]
    return it
