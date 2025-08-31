num a := 15
num b := 3

print("Soma: ", a + b)
print("Multiplicação: ", a * b)

fun dobrar(x) {
    x * 2
}

num resultado := { dobrar(10) }

print("Dobro de 10: ", resultado)

if (resultado > 15) -> {
    print("É maior que 15!")
}
