# ElsCap
We created the ElsCap dataset, meticulously compiled from a vast collection of open-access scientific articles on the ScienceDirect platform, a comprehensive repository of peer-reviewed academic literature managed by Elsevier.

## Project Structure
```
ELSCAP/
│
├── data/                  # Folder where the images will be saved.
|  ├── imgs/               # Folder for the images
|  ├── info/               # Folder for downloaded JSON files
│
├── main.py                # Entry point (orchestrates the process)
├── downloader_info.py     # Logic for downloading from Google Drive
├── processor.py           # Logic for reading JSONs, extracting URLs from images, and downloading them.
│
├── requirements.txt       # Required libraries (gdown, requests)
└── README.md              # Project documentation
```

- `main.py`: Entry point with a Command Line Interface (CLI).
- `downloader_info.py`: Manages Google Drive downloads and ZIP extraction.
- `processor.py`: Parses JSON metadata and handles image downloads via API.
- `data/`: Destination directory for organized downloaded images.

## JSON Metadata Structure

The script processes metadata extracted from scientific articles. The following image describes the data hierarchy:

![JSON Structure](./structure_json.png)

Key fields processed include:
- **Paper**: DOI and PII identifiers.
- **Figure**: Captions and figure types.
- **Image**: High-resolution URL for asset retrieval.
- **Paragraphs**: Contextual text surrounding figure citations.

## 🚀 Getting Started

### Prerequisites
Ensure you have the required libraries installed:
```bash
pip install gdown requests
```

### 🛠 Usage
You can run the script using different flags depending on your needs.

#### Full Pipeline (Recommended)
To download the ZIP from Drive, extract the folders, and download all images in one go:

```bash
python main.py --full --apikey "YOUR_API_KEY"
```

#### Download and Extract Only
If you only want to fetch the JSON files and organize the folders without downloading the images yet:

```bash
python main.py --download 
```

#### Process Existing Files
If you already have the JSON files in data/info/ and just need to download the images:

```bash
python main.py --process --apikey "YOUR_API_KEY"
```

#### Command Reference

| Argument | Description |
|-----------|-----------|
| `--download` | Downloads the ZIP from Drive, extracts it, and cleans up the temporary ZIP file. |
| `--process` | Iterates through the extracted JSON files and downloads images. |
| `--full` | Executes both `--download` and `--process` steps sequentially. |
| `--apikey` | The API key required to authorize image downloads from the provider.|

More information on obtaining the API key can be found here: https://dev.elsevier.com/