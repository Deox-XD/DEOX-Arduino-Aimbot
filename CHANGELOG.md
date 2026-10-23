# Changelog

All notable changes to DEOX will be documented in this file.

## [2.0.0] - 2024

### 🎨 Complete Rebrand
- Rebranded from ValorantArduinoColorbot to DEOX
- New professional visual identity
- Enhanced ASCII art and branding throughout

### ✨ Major Enhancements

#### Main Application (main.py)
- Beautiful color-coded terminal interface
- Real-time system information display
- Comprehensive configuration summary on startup
- Enhanced error handling with detailed messages
- Professional status indicators (✓/✗)
- Graceful shutdown handling

#### User Interface
- ANSI color support for better readability
- ASCII art DEOX logo
- Structured information display
- Session timestamp tracking
- Resolution and FOV information

#### Documentation (README.md)
- Complete documentation overhaul
- Professional markdown formatting with badges
- Comprehensive installation guide
- Detailed troubleshooting section
- Enhanced visual hierarchy
- Clear feature descriptions
- Usage tips and best practices
- Advanced configuration guide

#### Error Handling
- All error messages now DEOX branded
- Detailed troubleshooting guidance in error messages
- Color-coded status messages
- COM port detection improvements
- Better exception handling throughout

#### Configuration (settings.ini)
- Comprehensive inline documentation
- Tips and recommendations section
- Common keybind alternatives listed
- Performance tuning guidance
- Cleaner organization with section separators
- Detailed explanations for each parameter

#### Code Quality
- Professional docstrings throughout all modules
- Enhanced comments and explanations
- Improved architecture documentation
- Better code organization
- Type hints where applicable

#### Arduino Firmware
- Detailed communication protocol documentation
- Enhanced code comments
- Professional header with DEOX branding
- Improved code readability
- Better variable naming

#### Spoofer (spoofer.py)
- Beautiful startup interface
- Enhanced progress indicators
- Better error messages
- Improved user guidance
- Success/failure status reporting

### 🐛 Bug Fixes
- Improved serial port detection
- Better error handling for missing COM ports
- Fixed potential race conditions in mouse control
- Enhanced thread safety

### 🔧 Technical Improvements
- Optimized screen capture performance
- Better memory management
- Reduced CPU usage during idle
- Improved thread management
- Enhanced serial communication stability

### 📝 Documentation
- Added CONTRIBUTING.md
- Added LICENSE (MIT)
- Added CHANGELOG.md
- Added comprehensive .gitignore
- Updated all inline documentation

### 🎯 Features Maintained
- HSV-based color detection
- Arduino Leonardo hardware control
- VID/PID spoofing capability
- Multi-threaded aimbot/triggerbot
- Configurable FOV and speeds
- Humanized trigger delays
- Target offset for headshots

---

## [1.0.0] - Original Release

### Initial Features
- Basic color detection aimbot
- Arduino Leonardo integration
- Triggerbot functionality
- VID/PID spoofing
- Configuration via settings.ini
- Arduino CLI auto-download
