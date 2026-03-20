def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        x_new = x - f(x) / df(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x

# Example: solve x^2 - 2 = 0
f = lambda x: x**2 - 2
df = lambda x: 2*x

root = newton_raphson(f, df, 1.0)
print("Root:", root)
