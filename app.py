import gradio as gr
import cv2
import numpy as np
from predict import Predictor  # Import your Predictor class from predict.py
from ultralytics import YOLO
weights_path = "fpn_inception.h5"  # Change this to your model's weights file
model_name = ""  # Specify model name if necessary
predictor = Predictor(weights_path=weights_path, model_name=model_name, cpu=True)
yolo_model = YOLO("yolov8n.pt")
def deblur_and_detect(image):
    """
    Function to deblur an uploaded image using the Predictor class.
    """
    # Convert image to RGB format
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Call the Predictor
    deblurred = predictor(img_rgb, mask=None)
    deblurred_contiguous = np.ascontiguousarray(deblurred)
    results = yolo_model(deblurred_contiguous)
    annotated_image = results[0].plot()
    # Convert back to BGR format for display
    annotated_bgr = cv2.cvtColor(annotated_image, cv2.COLOR_RGB2BGR)
    return annotated_bgr
# Gradio Interface
interface = gr.Interface(
    fn=deblur_and_detect,
    inputs=gr.Image(type="numpy", label="Upload Blurry Image"),
    outputs=gr.Image(type="numpy", label="Deblurred Image with Object Detection"),
    title="Deblurring and Object Detection App",
    description="Upload a blurry image to deblur it and detect objects using YOLOv8."
)

if __name__ == "__main__":
    # Launch the app
    interface.launch()
