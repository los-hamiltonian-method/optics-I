import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Lente positivo
data = pd.read_csv('len_pos.csv')
f1s = (data['cota_i'] + data['cota_d']) / 2
errors_f1 = data['cota_i'] - data['cota_d']
# Olvidamos considerar 2cm
f1s = f1s + 2.9
print(f"{np.mean(f1s)} +/- {np.std(errors_f1) + 0.1}")


# Lente compuesto
def calculate_f2(bfl, f1, d):
	return (bfl * (f1 - d)) / (f1 - bfl - d)


def calculate_f2_ffl(ffl, f1, d):
	return (f1 * (d + ffl) - ffl * d) / (f1 - ffl)


# Lente compuesto D = 58.4
data2 = pd.read_csv('len_compuesto.csv')
# b es back focal length (bfl)
bs = (data2['b_i'] + data2['b_d']) / 2
# Distancia entre lentes
ds = data2['b+d'] - bs
# Diámetros de la imagen
diams = data2['diam']
print(ds.mean())

# La lente queda mejor con calculate_f2 entonces supongo que sí están bien las fórmulas
print(calculate_f2(bs.mean(), f1s.mean(), ds.mean()))
print(calculate_f2_ffl(bs.mean(), f1s.mean(), ds.mean()))
