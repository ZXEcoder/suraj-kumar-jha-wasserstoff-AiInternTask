import streamlit as st
from PIL import Image
import pandas as pd
from main import process_image
from ocr_utils import extract_image_as_whole
from summarizer_utils import summarize_object_data

st.title("YOLOv8 Object Detection and Text Extraction")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "bmp", "webp"])

if uploaded_file is not None:
    # Read the image file
    image_path = "uploaded_image.jpg"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.image(image_path, caption='Uploaded Image.', use_column_width=True)
    
    st.write("Processing Image...")
    results = process_image(image_path)
    
    # Display results
    st.write("### Extracted Data")
    
   

    df = pd.DataFrame(results)

    st.dataframe(df)
    txt = extract_image_as_whole(image_path)
    summary=summarize_object_data(txt)
    st.write("### Extracted Text")
    st.text(txt)
    st.write("### Summarized Text")
    st.text(summary)
    
    # Display segmented images
    st.write("### Segmented Images")
    output_dir = "output/"
    for obj in results:
        st.image(obj['image_path'], caption=obj['label'])
