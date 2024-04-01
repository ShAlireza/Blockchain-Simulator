import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def block_interval():
    xls = "blockchain.xlsx"
    block_interval_df = pd.read_excel(
            xls, sheet_name='Impact of Block Interval', skiprows=2
    ).rename(columns=lambda x: str(x).strip())
    print(block_interval_df.columns)
    block_interval_relevant_df = block_interval_df[
            ['Interval', 'mean', 'median', 'Bandwidth(kbps)']].copy()
    block_interval_relevant_df['Interval'] = pd.to_numeric(
            block_interval_relevant_df['Interval'].str.replace('s', ''),
            errors='coerce')
    block_interval_relevant_df['mean'] = pd.to_numeric(
            block_interval_relevant_df['mean'], errors='coerce')
    block_interval_relevant_df['median'] = pd.to_numeric(
            block_interval_relevant_df['median'], errors='coerce')
    block_interval_relevant_df['Bandwidth(kbps)'] = pd.to_numeric(
            block_interval_relevant_df['Bandwidth(kbps)'], errors='coerce')
    plt.figure(figsize=(15, 6))
    plt.plot(
            block_interval_relevant_df['Interval'],
            block_interval_relevant_df['Bandwidth(kbps)'],
            marker='o', linestyle='-', color='blue', label='Bandwidth')
    plt.title('Impact of Block Interval on Bandwidth')
    plt.xlabel('Block Interval (seconds)')
    plt.ylabel('Bandwidth(kbps)')
    plt.legend()
    plt.grid(True)
    plt.show()


def block_size():
    xls = "blockchain.xlsx"
    data = pd.read_excel(xls, sheet_name=None, skiprows=2)
    block_sizes = ["0.1MB", "0.25MB", "0.5MB", "1MB"]
    plt.figure(figsize=(15, 6))
    for size in block_sizes:
      x = data[size]["Interval"]
      y = data[size]["Bandwidth(kbps)"]
      plt.plot(x, y)

    plt.yticks(np.arange(0, 130000, 10000))
    plt.title("Block Size impact on Bandwidth")
    plt.xlabel("Block Interval")
    plt.ylabel("Bandwidth(kbps)")
    plt.legend(block_sizes)
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(15, 6))
    for size in block_sizes:
      x = data[size]["Interval"]
      y = data[size]["Sr"]
      plt.plot(x, y)

    plt.yticks(np.arange(0, 1.1, 0.1))
    plt.title("Block Size impact on Stale rate")
    plt.xlabel("Block Interval")
    plt.ylabel("Stale rate")
    plt.legend(block_sizes)
    plt.grid(True)
    plt.show()



if __name__ == "__main__":
    block_interval()
    block_size()
