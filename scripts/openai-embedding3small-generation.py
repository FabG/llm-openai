import pandas as pd

from openai import OpenAI
client = OpenAI()

embedding_model = "text-embedding-3-small"
embedding_encoding = "cl100k_base"
max_tokens = 8000  # the maximum for text-embedding-3-small is 8191
def get_embedding(text, model="text-embedding-3-small"):
   text = text.replace("\n", " ")
   return client.embeddings.create(input = [text], model=model).data[0].embedding

# load & inspect dataset
input_datapath = "data/fine_food_reviews_50.csv"
df = pd.read_csv(input_datapath, index_col=0)
df = df[["Time", "ProductId", "UserId", "Score", "Summary", "Text"]]
df = df.dropna()
df["combined"] = (
    "Title: " + df.Summary.str.strip() + "; Content: " + df.Text.str.strip()
)

print('fine review data sample: ' + df.head(2).to_string())

# get embeddings
# Ensure you have your API key set in your environment per the README: https://github.com/openai/openai-python#usage

# This may take a few minutes
df["embedding"] = df.combined.apply(lambda x: get_embedding(x, model=embedding_model))
# write to file
df.to_csv("data/fine_food_reviews_with_embeddings_50.csv")

print('fine review data sample with embeddings: ' + df.head(2).to_string())

