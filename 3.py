class PowerCalculator:
    def pow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.pow(x, -n)
        if n % 2 == 0:
            return self.pow(x * x, n // 2)
        else:
            return x * self.pow(x * x, (n - 1) // 2)

# Ejemplo de uso:
power_calculator = PowerCalculator()
result = power_calculator.pow(2, 5)
print("2^5 =", result)

result = power_calculator.pow(3, -3)
print("3^(-3) =", result)
