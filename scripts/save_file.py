import os
import pandas as pd


# Save the graphic in the file results
def save_file(save_path:str):
    if not os.path.exists('results'):
        os.makedirs('results')
    pd.plt.savefig(save_path)
    print(f"Graphic saved as '{save_path}'")
