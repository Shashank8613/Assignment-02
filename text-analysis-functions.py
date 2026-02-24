#1.count words
def count_words(text):
    words = text.split()
    return len(words)

#2. count vowels
def count_vowels(text):
    vowels = "aeiou"
    return sum(1 for char in text.lower() if char in vowels)

#3. count consonants
def count_consonants(text):
    vowels = "aeiou"
    return sum(1 for char in text.lower() if char.isalpha() and char not in vowels)

#4. reverse text
def reverse_text(text):
    return text[::-1]

#5. check palindrome (ignoring case and spaces)
def is_palindrome(text):
    normalized_text = text.replace(" ", "").lower()
    return normalized_text == normalized_text[::-1]

#6. remove vowels
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return "".join(char for char in text if char not in vowels)

#7. word frequency
def word_frequency(text):
    words = text.lower().split()
    frequency_dict = {}
    for word in words:
        frequency_dict[word] = frequency_dict.get(word, 0) + 1
    return frequency_dict

#8. find longest word
def longest_word(text):
    words = text.split()
    longest = max(words, key=len)
    return longest, len(longest)

#9. analyze text (main function)
def analyze_text(text):
    print("text analysis: ")
    print("words:", count_words(text))
    print("vowels:", count_vowels(text))
    print("consonants:", count_consonants(text))
    print("reversed:", reverse_text(text))
    print("palindrome:", "yes" if is_palindrome(text) else "no")
    print("without vowels:", remove_vowels(text))

    longest, length = longest_word(text)
    print(f"longest word: {longest} ({length} letters)")

    frequency = word_frequency(text)
    print("word Frequency:", end=" ")
    print(", ".join(f"{word}: {count}" for word, count in frequency.items()))


try:
    user_text = input("enter text: ")

    if not user_text:
        raise ValueError("text cannot be empty")

    analyze_text(user_text)

#exception handling
except ValueError as ve:
    print("Error: ",ve)

except Exception as e:
    print("Error: ", e)