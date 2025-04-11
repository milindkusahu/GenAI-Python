import tiktoken

encoder = tiktoken.encoding_for_model("gpt-4o")

print("Vocab Size", encoder.n_vocab) # Vocab Size 200019

text = "The cat sat on the mat"
tokens = encoder.encode(text)

print("Tokens:", tokens) # Tokens [976, 9059, 10139, 402, 290, 2450]

my_tokens =  [976, 9059, 10139, 402, 290, 2450]
decoded = encoder.decode(my_tokens)

print("Decoded Token:", decoded)