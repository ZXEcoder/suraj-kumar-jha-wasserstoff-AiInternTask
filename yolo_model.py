from ultralytics import YOLO

def load_yolo_model(model_path='yolov8x-seg.pt'):
    return YOLO(model_path)

def run_yolo_detection(model, image_path):
    return model(image_path)
