# plot_rolling_entropy.py
# Based on file_entropy.py and
# http://code.activestate.com/recipes/577476-shannon-entropy-calculation/#c4
# Takes a string of space-separated words at the beginning of the file. If 
# a file path is set, the text will be read from a file.
# The plot function uses 
import os
text = "" # Insert source text...
filepath = "" # ... or file path for input text
w = 100 # window size
output = "" # path to save output image

if filepath != "":
    f = open(filepath, "r")
    text = f.read()
    f.close()

def calculate_entropy(slice):
    import math
    text = " ".join(slice)
    byteArr = map(ord, text)
    fileSize = len(byteArr)

    # calculate the frequency of each byte value in the file
    freqList = []
    for b in range(256):
        ctr = 0
        for byte in byteArr:
            if byte == b:
                ctr += 1
        freqList.append(float(ctr) / fileSize)

    # Shannon entropy (min bits per byte-character)
    ent = 0.0
    for freq in freqList:
        if freq > 0:
            ent = ent + freq * math.log(freq, 2)
    ent = -ent
    return ent

def calculate_rolling_windows(text, w):
	text = text.split() # make it a list
	i = 0 # iterator
	series = []
	for x in text:
	    cut = i + w
	    slice = text[i:cut]
	    entropy = calculate_entropy(slice)
	    series.append(entropy)
	    i = i + 1
	#print series
	return series

def plot_rolling_windows(series):
	import matplotlib.pyplot as plt
	x = []
	for k,v in enumerate(series):
	    x.append(k)    
	y = series
	plt.plot(y)
	plt.savefig(output)
	plt.show() # Uncomment for ipython notebook use

series = calculate_rolling_windows(text, w)
plot_rolling_windows(series)