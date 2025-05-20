# Zadanie 1:
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
# Poprawiony błąd: Gdy n jest równe 0, funkcja powinna zwracać 1, a nie 0

# Testy:
def test_factorial():
    assert factorial(0) == 1
    assert factorial(3) == 6
    assert factorial(5) == 120