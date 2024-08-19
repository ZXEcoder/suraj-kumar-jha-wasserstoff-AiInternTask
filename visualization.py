import cv2
import matplotlib.pyplot as plt

def visualize_results(image_path, results):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    for r in results:
        boxes = r.boxes
        names = r.names
        
        for i, box in enumerate(boxes.xyxy):
            x1, y1, x2, y2 = box.int().numpy()
            class_id = int(boxes.cls[i].item())
            label = names[class_id]
            score = boxes.conf[i].item()
            
            cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)
            cv2.putText(image, f"{label} {score:.2f}", (x1, y1 - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    
    plt.imshow(image)
    plt.title("YOLOv8 Object Detection and Segmentation")
    plt.axis("off")
    plt.show()
