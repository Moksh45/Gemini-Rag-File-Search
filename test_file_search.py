from google import genai
from google.genai import types
import time
import os

client = genai.Client(api_key="api-key")

print("Starting File Search test...\n")

# Create the File Search store with a display name
print("1. Creating File Search store...")
file_search_store = client.file_search_stores.create(
    config={'display_name': 'test-file-search-store'}
)
print(f"   Created store: {file_search_store.name}\n")

# Upload and import a file into the File Search store
print("2. Uploading and importing sample.txt file...")
operation = client.file_search_stores.upload_to_file_search_store(
    file='sample.txt',
    file_search_store_name=file_search_store.name,
    config={
        'display_name': 'I, Claudius - Sample',
    }
)

# Wait until import is complete
print("   Waiting for import to complete...")
while not operation.done:
    time.sleep(2)
    operation = client.operations.get(operation)
    
print(f"   Import completed!\n")

# Ask a question about the file using File Search
print("3. Querying the file with a question about Robert Graves...")
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Can you tell me about Robert Graves and his work 'I, Claudius'?",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                file_search=types.FileSearch(
                    file_search_store_names=[file_search_store.name]
                )
            )
        ]
    )
)

print("Response from Gemini API:")
print("-" * 50)
print(response.text)
print("-" * 50)

# Display citation metadata if available
print("\nCitation metadata:")
if response.candidates and response.candidates[0].grounding_metadata:
    print(response.candidates[0].grounding_metadata)
else:
    print("No grounding metadata available")

# Clean up - delete the File Search store
print("\n4. Cleaning up - deleting File Search store...")
client.file_search_stores.delete(
    name=file_search_store.name,
    config={'force': True}
)
print(f"   Deleted store: {file_search_store.name}")

print("\nTest completed successfully!")
