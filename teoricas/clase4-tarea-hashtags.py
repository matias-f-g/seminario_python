posts = ["""post_The only Claude Code project structure you'll ever need 📁
Credit: codewithbrij
#ClaudeCode #Claude #Code #Python #PythonProgramming #Coding #Programming""",
"""⚡Daily Python Challenge⚡
Comment your answer now ⬇️,
Ready to level up your coding game? 🚀
#Python #PythonProgramming #Coding #Programming  #PythonChallenge #PythonQuiz""",
"""Take a few minutes to complete the 2026 Python Developers Survey and help us map out an accurate landscape of the Python community! #python #pythondevsurvey""",
"""30 Important AI Concepts
#Python #PythonProgramming #Coding #Programming #DataScience #MachineLearning #AI #DeepLearning"""
]

# SOLUTION N° 1: manually counting one by one with a dict

dict_counter = {}

for one_post in posts:
    for word in one_post.lower().split():
        if word.startswith("#"):
            dict_counter[word] = dict_counter.get(word, 0) + 1

dict_counter = dict(sorted(dict_counter.items(), key=lambda item:item[1], reverse=True))

print("\nResults of the first solution")
for h_word, h_count in dict_counter.items():
    print(h_word.ljust(20, "."), h_count)




# SOLUTION N° 2: create a list of hashtags and count them with Counter

from collections import Counter

hashtag_words = []

for one_post in posts:
    hashtag_words += [word for word in one_post.lower().split() if word.startswith("#")]

dict_counter = Counter(hashtag_words)

dict_counter = dict(sorted(dict_counter.items(), key=lambda item:item[1], reverse=True))

print("\n\nResults of the second solution")
for h_word, h_count in dict_counter.items():
    print(h_word.ljust(20, "."), h_count)




# SOLUTION N° 3: iterate the data word by word, selecting the ones that starts with a hashtag
#                and count them with Counter (the same module as before)


dict_counter = Counter(
    word
    for post in posts
    for word in post.lower().split()
    if word.startswith("#")
)

dict_counter = dict(sorted(dict_counter.items(), key=lambda item:item[1], reverse=True))

print("\n\nResults of the third solution")
for h_word, h_count in dict_counter.items():
    print(h_word.ljust(20, "."), h_count)