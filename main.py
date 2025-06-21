from exa_py import Exa
from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()

# Get the API key
api_key = os.getenv("EXA_API_KEY")

# Initialize Exa with the key
exa = Exa(api_key)

# Take user query input
query = input('Search here: ')

# Perform search
response = exa.search(
  query,
  num_results=5,
  type='keyword',
  include_domains=['https://open.spotify.com/'],
)

# Print results
for result in response.results:
  print(f'Title: {result.title}')
  print(f'URL: {result.url}')
  print()
