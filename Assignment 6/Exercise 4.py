def word_frequency(text):

    words = text.split()
    freq = {}

    for word in words:
        word = word.lower()

        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq


text = input("Enter text: ")

result = word_frequency(text)

sorted_words = sorted(result.items(), key=lambda x: x[1], reverse=True)

top5 = sorted_words[:5]

total_words = sum(result.values())

count_top5 = 0
for word in top5:
    count_top5 += word[1]

print("Top 5:", top5)
print("Total number of words:", total_words)

percent = count_top5 / total_words * 100
print("Proportion of 5 most common words:", percent, "%")