from sigfig import round

def round_down(x: int | str, sigfigs: int = 1) -> str:
    x = str(x)
    return x[0:sigfigs] + '0' * (len(x) - sigfigs)
