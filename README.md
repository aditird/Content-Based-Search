# FindImages: Intelligent Media Search System

FindImages is a Python-based system for processing and searching large volumes of media files using AWS Rekognition and OpenSearch. It enables content-based search (e.g., "person holding a sign") across thousands of photos and videos.

## 📌 Overview

This tool extracts metadata (e.g., labels, text, and facial attributes) from images using AWS Rekognition, indexes the metadata in OpenSearch, and allows users to search media content through keywords.

## 📁 Project Structure

```
FindImages/
├── process_media.py        # Processes media files and extracts metadata
├── search_images.py        # Implements search across indexed media
├── rekognition_utils.py    # AWS Rekognition utility functions
├── opensearch_utils.py     # OpenSearch indexing and query utilities
```

## ⚙️ Prerequisites

- Python 3.8+
- AWS credentials with Rekognition access
- An OpenSearch cluster (AWS or self-hosted)
- `boto3`, `requests`, `opensearch-py`, etc.

## 🚀 Setup & Usage

1. **Install dependencies**:

   ```bash
   pip install boto3 opensearch-py requests
   ```

2. **Configure environment**:
   - Ensure AWS credentials are configured (`~/.aws/credentials`)
   - Edit connection details in `opensearch_utils.py`

3. **Process media and index**:

   ```bash
   python process_media.py /path/to/media/folder
   ```

4. **Search images**:

   ```bash
   python search_images.py "query text here"
   ```

## 🔍 Sample Use Cases

- Search for photos with people, events, or branded items
- Index thousands of company event photos for fast retrieval
- Find "group selfie at night" or "person holding banner"

## 📦 Technologies Used

- AWS Rekognition
- OpenSearch
- Python (boto3, requests)

## 🛡️ License

This project is open-source under the MIT License.
