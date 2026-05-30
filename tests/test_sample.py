# Test edəcəyimiz sadə bir toplama funksiyası
def add(a, b):
    return a + b

# Uğurla keçməli olan test funksiyası (Adı mütləq test_ ilə başlamalıdır)
def test_add_success():
    assert add(10, 5) == 100
