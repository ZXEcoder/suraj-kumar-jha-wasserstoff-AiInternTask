# Suraj-Kumar-Jha-wasserstoff-AiInternTask YOLOv8 Object Detection, OCR, and Summarization Project

This project performs object detection using YOLOv8, extracts text from detected objects using Tesseract OCR, and summarizes the extracted text. The results, including the segmented objects and their corresponding extracted and summarized text, are saved to disk in dedicated folders.

## Project Structure

```
/my-project
│
├── data/                   # Folder to store input images
├── output/                 # Folder to store segmented images and output CSV
├── requirements.txt        # Python dependencies
├── app.py                  # Main entry point of the application
├── main.py                 # Core logic for processing images
├── yolo_model.py           # YOLOv8 model loading and detection
├── ocr_utils.py            # OCR utilities for text extraction
├── summarizer_utils.py     # Summarization utilities
├── visualization.py        # Visualization of results
└── README.md               # Project documentation
```

- **data/**: Contains input images to be processed.
- **output/**: Contains segmented object images and the final CSV output file.
- **requirements.txt**: Lists all Python dependencies required for the project.
- **app.py**: The main entry point of the application.
- **main.py**: Handles object detection, OCR, and summarization logic.
- **README.md**: Project documentation.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/ZXEcoder/suraj-kumar-jha-wasserstoff-AiInternTask.git
cd your-repo
```

### 2. Install Dependencies

Make sure you have Python installed, then install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### 3. Create Folders

Ensure you have the following folders created before running the application:
- **data/**: Place your input images in this folder.
- **output/**: The segmented images and the final output CSV file will be saved here.

You can create these folders with the following command:

```bash
mkdir data output
```

### 4. Run the Application

To process images, run the following command:

```bash
streamlit run app.py
```

This will start the application, which will load the images from the `data/` directory, process them using YOLOv8 for object detection and segmentation, extract text using Tesseract OCR, and summarize the text. The results will be saved in the `output/` directory.

## Usage

1. **Object Detection and Segmentation**: YOLOv8 is used to detect objects in images. Each detected object is cropped and saved as a separate image in the `output/` folder.
   
2. **Text Extraction**: Tesseract OCR is applied to each segmented image to extract text.

3. **Summarization**: Extracted text is summarized if it is long enough.

4. **Saving Results**: The results, including segmented images and a CSV file, are saved in the `output/` directory.

### Example Workflow

1. Place input images in the `data/` folder.
2. Run the script to process the images.
3. Segmented images will be saved in the `output/` folder.
4. A CSV file (`final_output_table.csv`) will be generated with object IDs, labels, extracted text, and summaries.

## Environment Setup

Ensure that Tesseract OCR is installed on your system:

- On Ubuntu, install Tesseract with:
  ```bash
  sudo apt-get install tesseract-ocr
  ```

- On macOS, install with Homebrew:
  ```bash
  brew install tesseract
  ```

- On Windows, download and install it from the official website.

You may also need to specify the Tesseract command path in your Python script:
```python
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'/path/to/tesseract'
```

## File Output

- **Segmented Object Images**: Detected objects are saved as images in the `output/` directory.
- **CSV File**: A CSV file is generated containing object IDs, labels, extracted text, and summaries.

### Example Output

After running the application, you should find the following files in the `output/` directory:

- `segmented_object_0_0.png`: Segmented object images.
- `final_output_table.csv`: A CSV file with the following columns:
  - `id`: Unique identifier for each segmented object.
  - `label`: Detected object label.
  - `extracted_text`: Text extracted from the object.
  - `summary`: Summarized text (if applicable).

## Known Issues

- **TesseractNotFoundError**: Make sure Tesseract OCR is installed and accessible via your system's PATH.
- **FileNotFoundError**: Ensure the `output/` directory exists or is created before saving results.

## Contributing

If you'd like to contribute to this project, feel free to submit a pull request. Make sure your contributions adhere to the coding standards and include proper documentation.

## DEMO

![OUTPUT](https://github.com/ZXEcoder/suraj-kumar-jha-wasserstoff-AiInternTask/blob/main/data/new.gif)

# LINK
### IF YOU WANT TO SEE DEPLOYED VERSION OF PROJECT CLICK THE LINK BELOW TO SEE AND TRY YOURSELF 👇
[HUGGING FACE DEPLOYED LINK](https://huggingface.co/spaces/SurajJha21/img_seg)

### If you want to see youtube video demo of project click the link down below to watch it 👇
[Youtube video Link](https://huggingface.co/spaces/SurajJha21/img_seg)

## License

This project is licensed under the MIT License.
