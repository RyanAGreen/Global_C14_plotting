from collections import Counter
def Binning_method(lower_bound, width, quantity):
   binning = []
   for low in range(lower_bound, lower_bound + quantity * width + 1, width):
      binning.append((low, low + width))
   return binning
def bin_assign(v, b):
   for i in range(0, len(b)):
      if b[i][0] <= v < b[i][1]:
         return i
the_bins = Binning_method(lower_bound=50,
   width=4,
   quantity=10)
print("The Bins: \n",the_bins)
weights_of_objects = [89.2, 57.2, 63.4, 84.6, 90.2, 60.3,88.7, 65.2, 79.8, 80.2, 93.5, 79.3,72.5, 59.2, 77.2, 67.0, 88.2, 73.5]
print("\nBinned Values:\n")
binned_weight = []
for val in weights_of_objects:
   index = bin_assign(val, the_bins)
   #print(val, index, binning[index])
   print(val,"-with index-", index,":", the_bins[index])
   binned_weight.append(index)
freq = Counter(binned_weight)
print("\nCount of values in each index: ")
print(freq)
