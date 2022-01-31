# line_equation

def line_equation(a, b, c):
    slope = (b[1]-a[1])/(b[0]-a[0])
    y_int = a[1]-slope*a[0]
    d = slope*c + y_int
    return d
