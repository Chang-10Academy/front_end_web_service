import os, sys

sys.path.append(os.path.abspath(os.path.join('scripts')))
from scripts import consumer1

data_received = consumer1.get_text_corpus
print(data_received)