import os
import numpy as np
import pandas as pd
from PIL import Image
from yolo_model import load_yolo_model, run_yolo_detection
from ocr_utils import extract_text_from_object
from summarizer_utils import summarize_object_data
from visualization import visualize_results
from ocr_utils import extract_image_as_whole

def extract_and_save_objects(image, results, output_dir="output/", format='PNG'):
    object_data = []
    image_pil = Image.fromarray(image)
    
    for i, r in enumerate(results):
        boxes = r.boxes
        names = r.names
        
        for j, box in enumerate(boxes.xyxy):
            x1, y1, x2, y2 = box.int().numpy()
            object_image = image_pil.crop((x1, y1, x2, y2))
            
            # Convert image mode if necessary
            if format in ['JPEG', 'JPG']:
                if object_image.mode in ['RGBA', 'LA']:
                    object_image = object_image.convert('RGB')
            elif format == 'PNG' and object_image.mode == 'RGB':
                object_image = object_image.convert('RGBA')
            
            # Save image with the correct format
            object_image_path = os.path.join(output_dir, f"segmented_object_{i}_{j}.{format.lower()}")
            object_image.save(object_image_path, format=format)
            
            class_id = int(boxes.cls[j].item())
            label = names[class_id]
            score = boxes.conf[j].item()
            
            obj_data = {
                "id": f"{i}_{j}",
                "box": [x1, y1, x2, y2],
                "image_path": object_image_path,
                "label": label,
                "score": score
            }
            object_data.append(obj_data)
    
    return object_data

def process_image(image_path):
    image = Image.open(image_path)
    image_np = np.array(image)
    
    model = load_yolo_model()
    print("Running YOLOv8 Segmentation and Object Detection...")
    results = run_yolo_detection(model, image_path)
    
    visualize_results(image_path, results)
    
    print("Extracting Objects...")
    object_data = extract_and_save_objects(image_np, results)
    
    print("Running Text Extraction...")
    for data in object_data:
        text = extract_text_from_object(data['image_path'])
        data['extracted_text'] = text
    
    print("Summarizing Object Attributes...")
    for data in object_data:
        text_for_summary = data.get('extracted_text', '')
        if len(text_for_summary) > 20:
            summary = summarize_object_data(text_for_summary)
            data['summary'] = summary
        else:
            data['summary'] = "Text too short for summarization"
    
    output_dir = "output/"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_table = pd.DataFrame(object_data, columns=['id', 'label', 'extracted_text', 'summary'])
    print("\nFinal Output Table:")
    print(output_table)

    output_table_path = os.path.join(output_dir, "final_output_table.csv")
    output_table.to_csv(output_table_path, index=False)
    
    print(f"Output table saved at {output_table_path}")

    return object_data
