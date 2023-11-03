import numpy as np
import matplotlib.pyplot as plt


word = str(input("Give me a word and I will count letters\n"))
n = (len(word))

# f(x) function 
def f(x):
    return n**((np.sin(x**np.sin(x**n))))
    
# plot that will use the amount of the characters of the string
x = np.linspace(0, 5, 10000)
y = f(x)
plotlabel = f'f(x) = {n}^(sin(x^sin(x^{n})))'
plt.plot(x, y, label=plotlabel)
# plot details
plt.axhline(0, color='black', linestyle='--', linewidth=1)
plt.axvline(0, color='black', linestyle='--', linewidth=1)

plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()

plt.show()
# minumum and maximum values shown 
y_min = np.min(y)
y_max = np.max(y)

print(f"Minimum value is {y_min}")
print(f"Maximum value is {y_max}")


# this part makes a graph that shows how many times each letter is in the string

letter_counts = {}

input_string = word.replace(" ", "").lower()

# go through the characters
for char in input_string:
    if char.isalpha():  # if it is a letter
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1

# Print the letter counts
for letter, count in sorted(letter_counts.items()):
    print(f"{letter} appears {count} times")

# a plot that shows the times each character appears
letters = sorted(letter_counts.keys())
counts = [letter_counts[letter] for letter in letters]

plt.bar(letters, counts)
plt.xlabel('Letters')
plt.ylabel('Times')
plt.title('Character Occurrences')
plt.show()