# multiplot_rolling_entropy.py
# Same as plot_rolling_entropy.py, but handles multiple files
import os
'''
Texts should be strings of space-separated words enclosed in quotes. 
Multiple text strings should be separated by commas. If a file path 
is added, the texts list will be ignored.
'''
#texts = []
texts = ["At London in Englonde noʒt fulle longe sythen Sythen Crist", 
         "suffride on crosse and Cristendome stabylde Ther was a byschop"]

'''
The file path may be a path to a single file or a single directory.
'''
filepath = "" # ... or file path for input text
w = 3 # window size
output = "" # path to save output image

if filepath != "":
    if isDir(filepath):
        files = os.listdir(filepath)
        for file in files:
            fp = os.path.join(filepath, file)
            f = open(fp, "r")
            texts.append(f.read())
            f.close()
    else:
        f = open(filepath, "r")
        texts.append(f.read())
        f.close()
else:
    texts.append(text)

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

def plot_rolling_windows(plots):
    import matplotlib.pyplot as plt
    for s in plots:
        x = []
        for k,v in enumerate(s):
            x.append(k)
        y = s
        plt.plot(y)
    plt.savefig(output)
    plt.show() # Uncomment for ipython notebook use

plots = []

for text in texts:
    series = calculate_rolling_windows(text, w)
    plots.append(series)

plot_rolling_windows(plots)