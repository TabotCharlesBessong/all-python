
sentence = "Hello men how are you doing  i just wanted to started machine learning today and i am not being able to download due to network issues"

result = {word:len(word) for word in sentence.split()}
print(result)