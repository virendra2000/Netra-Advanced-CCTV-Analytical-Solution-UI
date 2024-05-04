# Netra - Advanced CCTV Analytical Solution

Netra is an advanced video analytics solution designed to detect suspicious activities and potential threats in real-time from CCTV footage. It utilizes state-of-the-art computer vision and deep learning algorithms to identify and raise alarms for various dangerous scenarios, such as the presence of firearms, knives, or other weapons, as well as violent actions like assaults or attempted murders.

## Features

- **Object Detection**: Netra can accurately detect and classify various types of objects, including firearms, knives, and other potential weapons, enabling proactive threat identification.

- **Action Recognition**: The system is capable of recognizing and interpreting human actions and behaviors, such as aggressive movements, fighting, or brandishing weapons, allowing for timely intervention.

- **Real-Time Monitoring**: Netra continuously analyzes the incoming CCTV footage, providing instant alerts and notifications when a suspicious activity or potential threat is detected.

- **Alarm Integration**: The system can be integrated with existing security and alarm systems, automatically triggering alarms or notifying relevant authorities in case of detected threats.

- **Scalable Architecture**: Netra is designed to handle multiple CCTV streams simultaneously, making it suitable for deployment in large-scale environments, such as public spaces, commercial buildings, or industrial facilities.

- **User-Friendly Interface**: The solution provides an intuitive web-based interface for monitoring, configuring, and managing the system, ensuring easy operation and maintenance.

## Installation and Setup

1. Clone the repository:<br/>
```
https://github.com/virendra2000/Netra-Advanced-CCTV-Analytical-Solution-UI.git
```
2. Install the required dependencies:<br/>
```
pip install -r requirements.txt
```
3. Downloading the Weight File :<br/>
[![Download Netra](https://img.shields.io/badge/Download-Netra-brightgreen?style=for-the-badge)](https://drive.google.com/drive/folders/1HPvSmFC87HlSmb3N4gUnem89bC0QUhKL?usp=sharing)

4. Open the `detection.py` Change the Location of **CFG** and **WEIGHT** file in `detection.py` .
5. Change the Connection String and Database name and Collection name of your MongoDB Database in `detection.py`.
6. Run the application: `python main.py` 

## Contributing

We welcome contributions from the community! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For more information or inquiries, please contact [your-email@example.com].
