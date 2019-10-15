#%%
import matplotlib.pyplot as plt
filename = r'C:\Users\hp\Desktop\Mada\Homework\new\randomly.txt'
strdict = {}
with open(filename) as f:
    fileread = f.read()
    strings = fileread.split()
    for word in strings:
        if word in strdict:
            strdict[word] += 1
        else:
            strdict[word] = 1

counting = strdict.values()
indentation = list(range(1, len(counting) + 1))
plt.barh(indentation, counting, align='center', color=[0.6,0.3,0.2,0.9])
plt.ylabel("Word list")
plt.xlabel("Number of words")
plt.title("Word counting")
plt.yticks(indentation, strdict.keys())
plt.show()

print(strdict)
#I don't know how to sort it because when sorted the words and values don't match in the bar
