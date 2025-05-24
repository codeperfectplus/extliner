import os
from extliner.main import LineCounter
from pprint import pprint

# print("Testing line counting functionality...")
# result = count_lines(os.getcwd())
# print("Result:")
# pprint(result)

counter = LineCounter(ignore_extensions=[".py"])
result = counter.count_lines(os.getcwd())
print("JSON Output:")

print(counter.to_json(result))

print(type(counter.to_json(result)))