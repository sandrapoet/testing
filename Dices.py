def dices(dices: list[]): => int
    frecuencia ={}
    for dice in dices:
      frecuencia[dice]=frecuencia.get(dice,0)

print(frecuencia)
