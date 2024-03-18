# Alumno: Gabriel Sandoval   Ci: 30.866.625   Materia: Estructuras discretas 1 

import itertools
import tkinter as tk


def calcular_permutaciones(n, r):
    permutaciones = list(itertools.permutations(range(1, n+1), r))
    return permutaciones

def calcular_combinaciones(n, r):
    combinaciones = list(itertools.combinations(range(1, n+1), r))
    return combinaciones

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def calcular_arreglos(n, r):
    arreglos = factorial(n) // factorial(n - r)
    return arreglos

def calcular():
    n = int(entry_n.get())
    r = int(entry_r.get())

    if r > n:
        resultado_permutaciones.config(text="Error: r no puede ser mayor que n")
        resultado_combinaciones.config(text="")
        resultado_arreglos.config(text="")
        resultado_factorial.config(text="")
    else:

        permutaciones = calcular_permutaciones(n, r)
        combinaciones = calcular_combinaciones(n, r)
        arreglos = calcular_arreglos(n, r)
        fact_n = factorial(n)

    resultado_permutaciones.config(text=f"Permutaciones:\n{permutaciones}")
    resultado_combinaciones.config(text=f"Combinaciones:\n{combinaciones}")
    resultado_arreglos.config(text=f"Arreglos:\n{arreglos}")
    resultado_factorial.config(text=f"Factorial de n:\n{fact_n}")


# Crear la ventana
ventana = tk.Tk()
ventana.title("Calculadora de Permutaciones, Combinaciones y Arreglos")
ventana.geometry("650x400")  # Tamaño de la ventana

# Etiquetas y campos de entrada
label_n = tk.Label(ventana, text="Valor de n:")
label_n.pack()
entry_n = tk.Entry(ventana)
entry_n.pack()

label_r = tk.Label(ventana, text="Valor de r:")
label_r.pack()
entry_r = tk.Entry(ventana)
entry_r.pack()

# Botón para calcular
boton_calcular = tk.Button(ventana, text="Calcular", command=calcular)
boton_calcular.pack()

# Resultados
resultado_permutaciones = tk.Label(ventana, text="")
resultado_permutaciones.pack()

resultado_combinaciones = tk.Label(ventana, text="")
resultado_combinaciones.pack()

resultado_arreglos = tk.Label(ventana, text="")
resultado_arreglos.pack()

resultado_factorial = tk.Label(ventana, text="")
resultado_factorial.pack()

# Ejecutar la ventana
ventana.mainloop()
