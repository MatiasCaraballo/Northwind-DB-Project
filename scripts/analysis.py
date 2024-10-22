import pandas as pd
import matplotlib.pyplot as plt
import os

def create_plot(df,xlabel,ylabel,title,savepath):
    plt.figure(figsize=(10, 6))
    plt.plot(df[xlabel], df[ylabel], marker='o', linestyle='-', color='b')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)


    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"'{savepath}'.png")
    plt.show()
    # Guardar el gráfico en la carpeta 'results'
    if not os.path.exists('results'):
        os.makedirs('results')

    plt.savefig(savepath)
    print(f"Gráfico guardado como '{savepath}'")
