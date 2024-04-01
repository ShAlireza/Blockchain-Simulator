from math import floor
import matplotlib.pyplot as plt
delay_factors = ['1', '1.44', '2', '4']
delay_factors_percent = [str(floor(1/float(i) * 100) / 100 * 100)[:-2] + '%' for i in delay_factors]
total_average_traffic_per_node_delays = [697995, 720037, 595132, 720037]  # in Bytes

simulation_times_minutes_delays = [1000, 1440, 2000, 4000]

nodes_delays = 32

total_traffic_delays = [traffic * nodes_delays for traffic in total_average_traffic_per_node_delays]

simulation_times_seconds_delays = [time * 60 for time in simulation_times_minutes_delays]

throughput_delays_corrected = [traffic / time for traffic, time in zip(total_traffic_delays, simulation_times_seconds_delays)]
colors = ['#4daf4a', '#66c2a5', '#8da0cb', '#a6d854']  # Different shades of green (and some extra for variety)

plt.figure(figsize=(10, 6))
plt.bar(delay_factors_percent, throughput_delays_corrected, color=colors)

plt.title('Throughput for Different DDoS factors')
plt.xlabel('DDoS Factor')
plt.ylabel('Throughput (Bytes/s)')
plt.grid(axis='y', linestyle='--')

plt.show()

