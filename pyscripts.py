import matplotlib.pyplot as plt

# Define the block intervals and their corresponding simulation times in minutes
block_intervals = ['1000 min', '10 min', '100 min']
simulation_times = [100000, 1000, 10000]  # in minutes

# Define the total average traffic per node in bytes and number of nodes (from the reports)
total_average_traffic_per_node = [683865, 644411, 710168]  # in Bytes
nodes = 16

# Calculate total traffic for each simulation (traffic per node * number of nodes)
total_traffic = [traffic * nodes for traffic in total_average_traffic_per_node]

# Calculate throughput as total traffic / simulation time
# Convert simulation time to seconds for throughput calculation
throughput = [traffic / (time * 60) for traffic, time in zip(total_traffic, simulation_times)]

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(block_intervals, throughput, color=['blue', 'orange', 'green'])
plt.title('Network Throughput for Different Block Intervals')
plt.xlabel('Block Interval')
plt.ylabel('Throughput (Bytes/s)')
plt.grid(axis='y', linestyle='--')
plt.yscale('log')

plt.show()

