import cv2
import mysql.connector
import time
from ultralytics import YOLO

# Load the YOLO model
model = YOLO("yolov8n.pt")

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sravanthi123",
    database="object_detection"
)

cursor = connection.cursor()

# Open the webcam
cap = cv2.VideoCapture(0)

last_saved_time = 0

print("Real-time detection started!")
print("Press Q to stop.")

while True:
    success, frame = cap.read()

    if not success:
        print("Could not access the webcam.")
        break

    # Detect objects
    results = model(frame, verbose=False)

    # Display detections
    annotated_frame = results[0].plot()
    cv2.imshow("YOLO MySQL Detection", annotated_frame)

    # Save detections to MySQL once per second
    current_time = time.time()

    if current_time - last_saved_time >= 1:
        for box in results[0].boxes:
            class_id = int(box.cls[0])
            object_name = model.names[class_id]
            confidence = float(box.conf[0])

            cursor.execute(
                """
                INSERT INTO detections (object_name, confidence)
                VALUES (%s, %s)
                """,
                (object_name, confidence)
            )

        connection.commit()
        last_saved_time = current_time

    # Press Q to stop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
cursor.close()
connection.close()

print("Detection stopped. MySQL connection closed.")
