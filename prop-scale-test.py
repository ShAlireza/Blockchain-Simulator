import numpy as np
import matplotlib.pyplot as plt

# Define the delay factors and their corresponding block propagation times
delay_factors = ['1', '1.44', '2']
delay_factors_ddos = ['100%', '69%', '50%']
mean_block_propagation_times = [0.682688, 0.844055, 0.961979]
median_block_propagation_times = [0.698389, 0.794625, 0.742569]
percentile_10_block_propagation_times = [0.428493, 0.485031, 0.614742]
percentile_25_block_propagation_times = [0.633678, 0.660058, 0.635831]
percentile_75_block_propagation_times = [0.724939, 1.11043, 1.41952]
percentile_90_block_propagation_times = [0.739222, 1.14542, 1.43402]

x = np.arange(len(delay_factors))  # the label locations
width = 0.1  # the width of the bars

fig, ax = plt.subplots(figsize=(12, 8), facecolor='white')
rects1 = ax.bar(x - width*2, mean_block_propagation_times, width, label='Mean', color='#66c2a5')
rects2 = ax.bar(x - width, median_block_propagation_times, width, label='Median', color='#8da0cb')
rects3 = ax.bar(x, percentile_10_block_propagation_times, width, label='10th Percentile', color='#a6d854')
rects4 = ax.bar(x + width, percentile_25_block_propagation_times, width, label='25th Percentile', color='#4daf4a')
rects5 = ax.bar(x + width*2, percentile_75_block_propagation_times, width, label='75th Percentile', color='#b3de69')
rects6 = ax.bar(x + width*3, percentile_90_block_propagation_times, width, label='90th Percentile', color='#ccebc5')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('DDoS Factor')
ax.set_ylabel('Block Propagation Time (seconds)')
ax.set_title('Block Propagation Time by DDoS Factor')
ax.set_xticks(x)
ax.set_xticklabels(delay_factors_ddos)
ax.legend()

# Function to automatically label each bar
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(round(height, 2)),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=9)

# Apply the function to each bar set
autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)
autolabel(rects5)
autolabel(rects6)

fig.tight_layout()
plt.grid(axis='y', linestyle='--', color='grey', linewidth=0.75)
plt.show()

