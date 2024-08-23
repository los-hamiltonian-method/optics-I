import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('len_pos.csv')
dist_focales = (data['cota_i'] + data['cota_d'])/2
errors = data['cota_i'] - data['cota_d']
dist_focales = dist_focales + 2
print(f"{np.mean(dist_focales) + 2.9} +/- {np.std(errors) + 0.1}")


#Lente compuesto D = 58.4
