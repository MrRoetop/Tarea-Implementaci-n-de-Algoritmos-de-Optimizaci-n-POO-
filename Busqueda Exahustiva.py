import math

class OptimizadorBusquedaExhaustiva:
    """Clase para minimizar funciones en un intervalo mediante búsqueda exhaustiva."""
    
    def __init__(self, a: float, b: float, tolerancia: float):
        if a >= b:
            raise ValueError("El límite inferior debe ser menor que el superior.")
        self._a = a
        self._b = b
        self._tolerancia = tolerancia

    def optimizar(self, f):
        """Retorna (x_min, f_min) para la función f en el intervalo."""
        n = math.ceil((self._b - self._a) / self._tolerancia)
        h = (self._b - self._a) / n
        x_opt = self._a
        f_opt = f(x_opt)
        for i in range(1, n + 1):
            x = self._a + i * h
            fx = f(x)
            if fx < f_opt:
                f_opt = fx
                x_opt = x
        return x_opt, f_opt

def main():
    tolerancia = 0.001

    # Función 1: cuadrática
    f1 = lambda x: x**2 - 4*x + 4
    opt1 = OptimizadorBusquedaExhaustiva(0, 5, tolerancia)
    x1, y1 = opt1.optimizar(f1)
    print("=== Función Cuadrática ===")
    print("f(x) = x^2 - 4x + 4, intervalo [0,5]")
    print(f"Mínimo encontrado: x = {x1:.6f}, f(x) = {y1:.6f}")
    print(f"Valor real: x = 2.0, f(x) = 0")
    print(f"Error absoluto en x: {abs(x1 - 2.0):.6f}\n")

    # Función 2: trigonométrica
    f2 = lambda x: x + math.sin(x)
    opt2 = OptimizadorBusquedaExhaustiva(0, 10, tolerancia)
    x2, y2 = opt2.optimizar(f2)
    print("=== Función Trigonométrica ===")
    print("f(x) = x + sin(x), intervalo [0,10]")
    print(f"Mínimo encontrado: x = {x2:.6f}, f(x) = {y2:.6f}")
    print(f"Valor real: x = 0.0, f(x) = 0")
    print(f"Error absoluto en x: {abs(x2 - 0.0):.6f}\n")

    # Función 3: polinomial
    f3 = lambda x: x**4 - 14*x**3 + 60*x**2 - 70*x
    opt3 = OptimizadorBusquedaExhaustiva(0, 5, tolerancia)
    x3, y3 = opt3.optimizar(f3)
    print("=== Función Polinomial ===")
    print("f(x) = x^4 - 14x^3 + 60x^2 - 70x, intervalo [0,5]")
    print(f"Mínimo encontrado: x = {x3:.6f}, f(x) = {y3:.6f}")
    print(f"Valor real (mínimo global): x ≈ 0.7810, f(x) ≈ -24.3696")
    print(f"Error absoluto en x: {abs(x3 - 0.781):.6f}")

if __name__ == "__main__":
    main()
