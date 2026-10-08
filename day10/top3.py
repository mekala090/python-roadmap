import heapq

daily_temperatures = [18, 23, 16, 29, 25, 21, 27]

warmest_days = sorted(daily_temperatures, reverse=True)[:3]
print("Warmest temperatures (sorted):", warmest_days)
print("Warmest temperatures (heapq):", heapq.nlargest(3, daily_temperatures))