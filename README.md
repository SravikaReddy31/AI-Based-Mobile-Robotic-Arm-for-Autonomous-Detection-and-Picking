# AI-Based Mobile Robotic Arm (Raspberry Pi)

A low-cost **mobile robotic arm** capable of **object detection, navigation, and pick-and-place operations** using a Raspberry Pi. The system integrates **computer vision, motor control, and servo-based manipulation** and supports both **manual** and **automatic (AI)** modes.

---

##  Overview

This project demonstrates a compact, cost-effective solution for **warehouse automation and smart robotics**.
The robot can:

* Move in different directions using a 4-wheel chassis
* Control a multi-DOF robotic arm (base, shoulder, joint, gripper)
* Detect objects using a camera (AI module)
* Pick and place objects autonomously

---

##  Features

*  **Mobile Platform** – 4 DC motors with mecanum wheels
*  **Robotic Arm** – 4 servo motors (gripper + joints)
*  **AI Object Detection** (planned/optional)
*  **Dual Mode Operation**

  * Manual (keyboard control)
  * Automatic (AI-based)
*  **Low-Cost Prototype**
*  Modular and expandable design

---

##  Hardware Components

* Raspberry Pi 5
* L298N Motor Driver
* 4 × DC Motors (Mecanum wheels)
* 4 × MG90S Servo Motors
* Web cam
* Battery Pack (for motors)
* External 5V supply (recommended for servos)
* Robot chassis + robotic arm kit

---

##  Connections

### Motor Driver → Raspberry Pi

| Motor Driver | Raspberry Pi GPIO |
| ------------ | ----------------- |
| IN1          | GPIO17            |
| IN2          | GPIO27            |
| IN3          | GPIO22            |
| IN4          | GPIO23            |
| GND          | GND               |

### Motor Driver → Motors

| Output      | Motors                |
| ----------- | --------------------- |
| OUT1 + OUT2 | Left side (DC1, DC2)  |
| OUT3 + OUT4 | Right side (DC3, DC4) |

> Ensure both motors on each side rotate in the same direction. Reverse wiring of one motor if needed.

### Servo Connections

| Servo  | Function | GPIO   |
| ------ | -------- | ------ |
| Servo1 | Gripper  | GPIO18 |
| Servo2 | Joint    | GPIO19 |
| Servo3 | Shoulder | GPIO20 |
| Servo4 | Base     | GPIO21 |

**Servo wiring:**

* Red → 5V
* Brown → GND
* Orange → GPIO

 Use external 5V for servos if possible.
 All grounds must be common.

---

##  Software Requirements

* Python 3.x
* RPi.GPIO
* OpenCV (camera handling and image processing)
* YOLO (object detection model)
* NumPy

Install dependencies:

```bash
sudo apt update
sudo apt install python3-opencv
pip install numpy
```

---

##  Usage

### Run Wheel Control

```bash
python3 wheels.py
```

### Run Arm Control

```bash
python3 arm_control.py
```

### Run Full Robot Control

```bash
python3 robot_control.py
```

---

##  Controls (Manual Mode)

| Key | Action           |
| --- | ---------------- |
| f   | Forward          |
| b   | Backward         |
| l   | Left             |
| r   | Right            |
| s   | Stop             |
| 1   | Gripper open     |
| 2   | Gripper close    |
| 3/4 | Shoulder up/down |
| 5/6 | Base left/right  |
| 7/8 | Joint up/down    |

---

##  Working Methodology

1. Camera captures the environment
2. Raspberry Pi processes input (AI / manual)
3. Control signals sent to motor driver
4. Robot navigates toward object
5. Servo motors position the arm
6. Gripper picks and places the object

---

##  Results

* Robot successfully moves in all directions
* Robotic arm performs gripping actions
* Servo motors provide precise movement
* Prototype demonstrates pick-and-place capability

---

##  Current Status

* ✅ Wheel movement working
* ✅ Motor driver integration completed
* ✅ Servo testing in progress
* 🔄 AI object detection integration in progress

---

##  Future Enhancements

* Real-time object detection (YOLO / OpenCV)
* Autonomous navigation
* Obstacle avoidance
* Mobile app / web control
* Voice control integration

---

##  Applications

* Warehouse automation
* Industrial material handling
* Smart robotics systems
* Educational robotics projects

---


##  Acknowledgment

This project is developed as part of an academic robotics initiative to demonstrate **practical AI-based automation systems**.

---

##  Contact

Your Name: Sravika Reddy
Project: AI Mobile Robotic Arm

---

 If you like this project, consider giving it a star!
