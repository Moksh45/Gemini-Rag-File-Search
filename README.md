# Gemini RAG File Search

A Python implementation demonstrating Google Gemini's File Search API for Retrieval Augmented Generation (RAG). This project shows how to upload files to a File Search store, index them with embeddings, and query them using semantic search.

## Overview

This project demonstrates:
- Creating a File Search store in the Google Gemini API
- Uploading and importing files for indexing
- Querying files using semantic search
- Retrieving citations and grounding metadata
- Cleaning up resources after use

## Prerequisites

- Python 3.8 or higher
- A Google Gemini API key (get one from [Google AI Studio](https://aistudio.google.com/apikey))
- Internet connection for API calls

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Moksh45/Gemini-Rag-File-Search.git
cd Gemini-Rag-File-Search
```

2. Create a virtual environment:
```bash
python -m venv .venv
```

3. Activate the virtual environment:
```bash
# On macOS/Linux:
source .venv/bin/activate

# On Windows:
.venv\Scripts\activate
```

4. Install required dependencies:
```bash
pip install google-genai
```

## Configuration

### Setting Your API Key

Before running the script, you need to set your Google Gemini API key. Edit `test_file_search.py` and replace `"api-key"` with your actual API key:

```python
client = genai.Client(api_key="YOUR_ACTUAL_API_KEY_HERE")
```

Alternatively, you can use an environment variable:

```python
import os
api_key = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key)
```

Then export the environment variable before running:
```bash
export GOOGLE_API_KEY="your-api-key-here"
```

## Running the Test

1. Make sure you're in the project directory and the virtual environment is activated:
```bash
cd /Users/link/Documents/link/google-rag
source .venv/bin/activate
```

2. Run the test script:
```bash
python test_file_search.py
```

### Expected Output

The script will:
1. Create a new File Search store
2. Upload and import `sample.txt` file
3. Wait for the import to complete (may take a few seconds)
4. Query the file with a question about Robert Graves
5. Display the response with citations
6. Show grounding metadata showing which parts of the document were used
7. Clean up by deleting the File Search store
8. Print success message

Example output:
```
Starting File Search test...

1. Creating File Search store...
   Created store: fileSearchStores/testfilesearchstore-xxxxx

2. Uploading and importing sample.txt file...
   Waiting for import to complete...
   Import completed!

3. Querying the file with a question about Robert Graves...
Response from Gemini API:
--------------------------------------------------
[AI response with citations...]
--------------------------------------------------

Citation metadata:
[Grounding chunks and metadata...]

4. Cleaning up - deleting File Search store...
   Deleted store: fileSearchStores/testfilesearchstore-xxxxx

Test completed successfully!
```

## Files

- `test_file_search.py` - Main test script demonstrating File Search functionality
- `sample.txt` - Sample document about "I, Claudius" by Robert Graves
- `README.md` - This file with instructions

## API Models

The script uses the following models:
- **gemini-2.5-flash** - For content generation with File Search

### Supported File Formats

File Search supports various file formats including:
- Text files (.txt, .md, .pdf, .doc, .docx, etc.)
- Spreadsheets (.csv, .xlsx, .xls)
- And more (see [Google Gemini docs](https://ai.google.dev/gemini-api/docs/file-search#supported_file_formats))

## How File Search Works

1. **Upload & Import**: Files are uploaded and automatically chunked
2. **Embedding**: Content is converted to embeddings for semantic search
3. **Indexing**: Embeddings are stored in the File Search store
4. **Query**: User queries are converted to embeddings and matched against stored content
5. **Retrieval**: Relevant chunks are retrieved and used as context for the model

## Citation & Grounding

The API returns grounding metadata that shows:
- Which chunks from your files were used in the response
- Exact text segments that were used
- Segment indices for precise location tracking

This helps verify that the model's response is based on your actual documents.

## Troubleshooting

### "Missing key inputs argument" Error
- Make sure you've set a valid API key in the script
- Check that your API key doesn't have any extra spaces or quotes

### "File not found" Error
- Make sure `sample.txt` is in the same directory as the script
- Check the file path is correct

### Operation timeout
- The import process may take longer for large files
- Increase the `time.sleep()` duration in the while loop if needed
- Check your internet connection

### Rate limit errors
- The Gemini API has rate limits
- Wait a moment before running the script again
- Refer to [rate limit docs](https://ai.google.dev/gemini-api/docs/rate-limits)

## Pricing

- **Indexing**: $0.15 per 1M tokens (for embeddings)
- **Storage**: Free
- **Queries**: Retrieved tokens counted as context tokens at standard rates

See [pricing documentation](https://ai.google.dev/gemini-api/docs/pricing#gemini-embedding) for details.

## Resources

- [Google Gemini API Documentation](https://ai.google.dev/gemini-api/docs)
- [File Search API Reference](https://ai.google.dev/gemini-api/docs/file-search)
- [API Keys Guide](https://ai.google.dev/gemini-api/docs/api-key)
- [Google AI Studio](https://aistudio.google.com/apikey)

## License

This project is licensed under the Apache 2.0 License.

## Support

For issues with the Google Gemini API, visit:
- [Gemini API Discussions](https://discuss.ai.google.dev/c/gemini-api/)
- [Issue Tracker](https://github.com/Moksh45/Gemini-Rag-File-Search/issues)

---

**Last Updated**: November 17, 2025
