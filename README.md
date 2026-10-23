# 🎯 DEOX - Advanced Colorbot System

<div align="center">

![DEOX](https://img.shields.io/badge/DEOX-Colorbot-blueviolet?style=for-the-badge)
![Version](https://img.shields.io/badge/version-2.0-blue?style=for-the-badge)
![Arduino](https://img.shields.io/badge/Arduino-Leonardo-00979D?style=for-the-badge&logo=arduino)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python)

**Advanced Arduino-Based Color Detection & Aim Assistance System**

</div>

---

## ⚠️ IMPORTANT DISCLAIMER

> **This software is provided for EDUCATIONAL PURPOSES ONLY**

- ❌ **Anti-Cheat Detection**: DEOX is **NOT** designed to bypass anti-cheat systems and makes **NO** attempt to do so
- ⚙️ **Hardware Compatibility**: Requires **Arduino Leonardo** board (other boards are NOT supported)
- ⚖️ **Legal Responsibility**: The developer assumes **ZERO** responsibility for:
  - Account suspensions or permanent bans
  - Violations of game Terms of Service
  - Any legal consequences from misuse
  - Damage to hardware or software

**By using DEOX, you acknowledge all risks and accept full responsibility for any consequences.**

---

## 🚀 Features

✨ **Advanced Features**
- 🎯 **Precision Aimbot**: HSV-based color detection with customizable FOV
- 🔫 **Smart Triggerbot**: Humanized delays and configurable trigger zones
- 🎮 **Arduino Integration**: Hardware-level mouse control for enhanced stability
- ⚡ **High Performance**: Optimized screen capture and multi-threaded processing
- 🛠️ **Fully Configurable**: Extensive customization via `settings.ini`
- 🔒 **VID/PID Spoofing**: Advanced Arduino identification masking

---

## 📋 Requirements

### Hardware
- 🔌 **Arduino Leonardo** board
- 🖱️ USB mouse (for VID/PID extraction)
- 💻 Windows 10/11 (64-bit)

### Software
- 🐍 Python 3.8 or higher
- 🎮 Target game with enemy highlight color set to **Purple**

---

## 📦 Installation Guide

### Step 1: Install Python Dependencies

Open PowerShell or Command Prompt and run:

```powershell
pip install -r requirements.txt
```

**Dependencies installed:**
- `opencv-python` - Image processing
- `numpy` - Numerical operations
- `mss` - Fast screen capture
- `pyautogui` - Screen utilities
- `pyserial` - Arduino communication
- `pywin32` - Windows API access
- `requests` - HTTP requests

---

### Step 2: Configure Arduino Leonardo

Run the DEOX spoofer to configure your Arduino:

```powershell
python spoofer.py
```

**What this does:**
1. 📥 Downloads Arduino CLI automatically
2. 🔍 Detects connected mouse devices
3. 🎭 Applies VID/PID spoofing to Arduino
4. ⚡ Compiles and uploads firmware
5. ✅ Validates successful deployment

**Follow the on-screen prompts:**
- Select your primary mouse from the list
- Enter Arduino COM port (e.g., `COM3`)
- Wait for upload completion

---

### Step 3: Configure Settings

Edit `settings.ini` to customize DEOX behavior:

```ini
[Settings]
COM-Port = COM3  # Your Arduino port

[Aimbot]
Enabled = true
toggleKey = 0x02        # Right Mouse Button
xSpeed = 0.4            # Horizontal aim speed
ySpeed = 0.4            # Vertical aim speed
xFov = 100              # Horizontal field of view
yFov = 75               # Vertical field of view
targetOffset = 8.0      # Vertical target offset (headshot adjustment)

[Triggerbot]
Enabled = true
toggleKey = 0xA4        # Left Alt key
minDelay = 75           # Minimum shoot delay (ms)
maxDelay = 125          # Maximum shoot delay (ms)
xRange = 15             # Horizontal trigger zone
yRange = 15             # Vertical trigger zone
```

**Keybind Reference**: [Windows Virtual-Key Codes](https://learn.microsoft.com/windows/win32/inputdev/virtual-key-codes)

---

### Step 4: In-Game Configuration

⚙️ **Required Game Settings:**

1. **Sensitivity**: Set to **0.5** (critical for accuracy)
2. **Enemy Highlight Color**: Change to **Purple** (exact match required)
3. **Graphics**: Medium-High settings recommended for consistent detection
4. **Display Mode**: Fullscreen or Borderless Window

---

### Step 5: Launch DEOX

Start the colorbot system:

```powershell
python main.py
```

**Status Indicators:**
- ✅ Green text: System operational
- 🔴 Red text: Error detected
- 📊 FPS counter: Performance monitor

---

## 🎮 Usage

### Controls

| Key | Function | Default |
|-----|----------|---------|
| **Right Mouse Button** | Activate Aimbot | Hold to track targets |
| **Left Alt** | Activate Triggerbot | Hold to auto-fire |
| **Close Terminal** | Exit DEOX | Terminates all processes |

### Operation Tips

💡 **Best Practices:**
- 🎯 Start with lower speed values (0.3-0.5) and adjust up
- 🔍 Reduce FOV in close-quarters maps
- ⏱️ Increase triggerbot delays for more natural behavior
- 🎨 Ensure purple enemy outlines are clearly visible
- 💻 Close unnecessary applications for better performance

---

## 🛠️ Troubleshooting

### Common Issues

**Arduino not detected:**
```powershell
# Check connected COM ports
mode
# Or use Device Manager → Ports (COM & LPT)
```

**Python dependency errors:**
```powershell
# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

**Detection not working:**
- Verify enemy outline color is **exactly purple**
- Check FOV settings aren't too restrictive
- Ensure game is in focus
- Try adjusting `targetOffset` value

**Serial port already in use:**
- Close Arduino IDE or Serial Monitor
- Restart DEOX application
- Check for other Python processes

---

## 📁 Project Structure

```
DEOX/
├── 📄 main.py              # Application entry point
├── 🎯 colorbot.py          # Core detection & control logic
├── 🖱️ mouse.py             # Arduino serial communication
├── 📸 capture.py           # Screen capture module
├── ⚙️ settings.py          # Configuration manager
├── 🎭 spoofer.py           # Arduino VID/PID spoofer
├── 📋 settings.ini         # User configuration
├── 📦 requirements.txt     # Python dependencies
├── 📖 README.md            # Documentation
└── 🔧 arduino/
    └── arduino.ino         # Arduino firmware
```

---

## 🔧 Advanced Configuration

### Color Detection Tuning

Edit `colorbot.py` to adjust HSV color ranges:

```python
# Purple detection (default)
self.lower_color = np.array([150, 76, 123])
self.upper_color = np.array([160, 197, 255])
```

Use HSV color picker tools to find optimal values for your setup.

---

## 🤝 Contributing

Contributions to improve DEOX are welcome! Please ensure:
- Code follows PEP 8 style guidelines
- All features are thoroughly tested
- Documentation is updated accordingly

---

## 📜 License

This project is provided **AS-IS** with no warranty. Use at your own risk.

Educational and research purposes only. Not affiliated with or endorsed by any game developer or publisher.

---

## 🎖️ Credits

**DEOX System** - Developed and maintained by **Deox**

Original concept: ValorantArduinoColorbot
Enhanced and rebranded as DEOX with advanced features and improved codebase.

---

<div align="center">

**⚡ Powered by DEOX Technology ⚡**

Made with 💜 for the community

</div>
