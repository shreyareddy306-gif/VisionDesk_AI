# check_model.py
from ultralytics import YOLO
<<<<<<< HEAD
import os
import sys

print("=" * 60)
print("🔍 YOLO Model Diagnostics")
print("=" * 60)

model_path = 'ppe_yolov8.pt'
if not os.path.exists(model_path):
    print(f"❌ Model file not found at: {model_path}")
    sys.exit(1)

model = YOLO(model_path)

print("\n📋 Model Classes Index:")
print("-" * 40)
for idx, name in model.names.items():
    print(f"   ID {idx}: '{name}'")

# Test on a target image if provided, or search upload directory
test_image = None
if len(sys.argv) > 1:
    test_image = sys.argv[1]
elif os.path.exists('uploads') and len(os.listdir('uploads')) > 0:
    for f in os.listdir('uploads'):
        if f.lower().endswith(('.jpg', '.jpeg', '.png')):
            test_image = os.path.join('uploads', f)
            break

if test_image and os.path.exists(test_image):
    print(f"\n🧪 Running test inference on: {test_image}")
    results = model(test_image, conf=0.20, imgsz=640)
    
    print(f"\n📊 Detections Found: {len(results[0].boxes)}")
    for box in results[0].boxes:
        cls_name = model.names[int(box.cls[0])]
        conf = float(box.conf[0])
        print(f"   - Detected '{cls_name}' with confidence: {conf:.2f}")
    
    results[0].save('test_result.jpg')
    print("\n✅ Annotated diagnostic image saved as: test_result.jpg")
else:
    print("\n⚠️ No test images found in 'uploads/'. Place a test image in the project directory to verify bounding boxes.")

print("=" * 60)
=======
import cv2
import numpy as np
import os

print("=" * 60)
print("🔍 YOLO Model Check")
print("=" * 60)

# Load model
model_path = 'ppe_yolov8.pt'
if not os.path.exists(model_path):
    print(f"❌ Model not found at: {model_path}")
    print("   Please make sure 'ppe_yolov8.pt' is in the project folder")
    exit()

model = YOLO(model_path)

print("\n📋 Available Classes in Your Model:")
print("-" * 40)
for idx, name in model.names.items():
    print(f"   {idx}: {name}")

print("\n" + "=" * 60)
print("🧪 Testing with a sample image...")

# Create a simple test image with a person-like shape
img = np.zeros((480, 640, 3), dtype=np.uint8)
# Draw a simple person shape
cv2.rectangle(img, (250, 200), (290, 400), (200, 200, 200), -1)  # Body
cv2.circle(img, (270, 180), 30, (200, 200, 200), -1)  # Head
cv2.rectangle(img, (240, 280), (300, 290), (100, 100, 100), -1)  # Belt

# Save test image
cv2.imwrite('test_person.jpg', img)
print("   Created test image: test_person.jpg")

# Run detection
results = model('test_person.jpg', conf=0.25)
print(f"\n📊 Detection Results:")
print(f"   Objects detected: {len(results[0].boxes)}")

for box in results[0].boxes:
    cls = model.names[int(box.cls[0])]
    conf = float(box.conf[0])
    print(f"   - {cls} (confidence: {conf:.2f})")

if len(results[0].boxes) == 0:
    print("\n❌ No objects detected in test image!")
    print("   This means your model might not recognize people.")
    print("   Try using a different model or check the model file.")

# Show annotated image
annotated = results[0].plot()
cv2.imwrite('test_result.jpg', annotated)
print("\n✅ Annotated result saved as: test_result.jpg")

print("=" * 60)

>>>>>>> 4eb6a0792b22b4c4da81d2188e1c97efe15fc32a
