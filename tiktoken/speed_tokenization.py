from time import perf_counter
import tiktoken

encoder = tiktoken.get_encoding("cl100k_base")

start_time = perf_counter()

token_count = 0
for i in range(100000):
    tokens = encoder.encode("The quick brown fox jumps over the lazy dog.")
    token_count += len(tokens)

end_time = perf_counter()

seconds = end_time-start_time

print("Tokens:", token_count)
print("Time:", seconds, "seconds")

speed = int(token_count / seconds)
print(speed, "tokens per second")
