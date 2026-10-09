Real-Time Object Detection & Logging Platform

📌 Project Overview

The Real-Time Object Detection & Logging Platform is a computer vision application that detects objects in real time using a webcam. It uses the YOLO object detection model and OpenCV to identify objects, stores detection records in a MySQL database, and displays detection information through a Streamlit dashboard.

🎯 Objectives

- Detect objects in real time using a webcam.
- Identify objects and their confidence scores using YOLO.
- Store detection details in a MySQL database.
- Display detection records and statistics on an interactive dashboard.
- Filter and analyze previously recorded detections.

🛠️ Technologies Used

- Python — Application development
- YOLO (Ultralytics) — Object detection
- OpenCV — Webcam and video processing
- MySQL — Database storage
- Streamlit — Interactive dashboard
- Pandas — Data processing

📂 Project Structure

Real-Time-Object-Detection/
├── dashboard.py
├── realtime_detection_mysql.py
├── requirements.txt
├── .gitignore
└── README.md

⚙️ Requirements

- Python 3.10 or another version supported by the installed dependencies
- MySQL Server
- A webcam
- Internet connection for installing the required Python packages

🚀 Installation and Setup

1. Clone the repository

git clone https://github.com/YOUR-USERNAME/Real-Time-Object-Detection.git
cd Real-Time-Object-Detection

Replace "YOUR-USERNAME" with your GitHub username.

2. Create a virtual environment

python -m venv .venv

Activate it on Windows:

.venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

4. Configure the MySQL database

Open MySQL and execute:

CREATE DATABASE object_detection;
USE object_detection;

CREATE TABLE detections (
    id INT AUTO_INCREMENT PRIMARY KEY,
    object_name VARCHAR(100),
    confidence FLOAT,
    detected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

Configure the MySQL connection settings in the application using your own database credentials. Do not publish your database password in the repository.

5. Run real-time object detection

python realtime_detection_mysql.py

Allow access to your webcam if prompted. Detected objects are recorded in the MySQL database.

Press Q in the detection window to quit, if supported by the application.

6. Launch the dashboard

Open another terminal in the project folder, activate the virtual environment, and run:

streamlit run dashboard.py

Streamlit will display a local URL in the terminal. Open that URL in your browser to view the dashboard.

📊 Features

- Real-time object detection
- Object classification and confidence scores
- MySQL-based detection logging
- Interactive Streamlit dashboard
- Detection history and filtering
- Summary statistics and visual charts

🔒 Security

Database credentials should be stored securely and must not be committed to a public repository. The ".gitignore" file excludes selected local files and environment-specific folders.

🔮 Future Enhancements

- Add support for uploaded images and video files.
- Export detection reports.
- Add user authentication.
- Deploy the dashboard to a suitable hosting platform.
- Improve analytics and historical detection visualizations.

👩‍💻 Author

Developed as an academic project on real-time object detection and logging.

📄 License

This project is intended for educational and demonstration purposes.
