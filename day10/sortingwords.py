products = ["tea", "coffee", "milk", "bread", "rice"]

# Sort by name length, then alphabetically when lengths match.
sorted_products = sorted(products, key=lambda product: (len(product), product))
print(sorted_products)

import heapq

scores = [72, 95, 88, 64, 100, 91, 83]
top_three = sorted(scores, reverse=True)[:3]
print("Top 3 (sorted):", top_three)
print("Top 3 (heapq):", heapq.nlargest(3, scores))