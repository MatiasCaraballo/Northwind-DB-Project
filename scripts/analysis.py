import pandas as pd
import matplotlib.pyplot as plt

class analysis:
    def create_plot(df,xlabel:str,ylabel:str,title:str,savepath:str):
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
       
