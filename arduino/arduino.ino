/*
╔═══════════════════════════════════════════════════════════╗
║              DEOX ARDUINO FIRMWARE v2.0                   ║
║        Hardware-Level Mouse Control via Leonardo         ║
║                                                           ║
║  Developer: Deox                                          ║
║  Board: Arduino Leonardo                                  ║
║  Protocol: Serial @ 115200 baud                           ║
╚═══════════════════════════════════════════════════════════╝
*/

#include <Mouse.h>

// Communication protocol command buffer
String command = "";  // Received command from Python client
int deltaX = 0, deltaY = 0;  // Mouse movement deltas

// Click state management for humanized behavior
bool isClicking = false;  // Active click flag
unsigned long clickStartTime = 0;  // Click initiation timestamp
unsigned long clickDuration;  // Randomized click duration (40-80ms)

void setup() {
    // Initialize high-speed serial communication
    Serial.begin(115200);  // 115200 baud for minimal latency
    Serial.setTimeout(1);  // 1ms timeout for responsive reads
    
    // Initialize USB HID mouse interface
    Mouse.begin();
    
    // Seed PRNG for click duration randomization
    randomSeed(analogRead(0));  // Use floating analog pin for entropy
    
    // Startup indication (optional - remove if causing issues)
    // Can be used to verify Arduino is ready
}

void loop() {
    // Process incoming serial commands (non-blocking)
    if (Serial.available() > 0) {
        // Read command until newline delimiter
        command = Serial.readStringUntil('\n');
        command.trim();  // Strip whitespace

        // Command: M<x>,<y> - Mouse movement
        if (command.startsWith("M")) {
            int commaIndex = command.indexOf(',');  // Find the position of the comma
            // Make sure the command is formatted correctly
            if (commaIndex != -1) {
                // Extract the movement values for X and Y axes
                deltaX = command.substring(1, commaIndex).toInt();  // Get X-axis movement
                deltaY = command.substring(commaIndex + 1).toInt();  // Get Y-axis movement

                // Move the mouse incrementally to prevent sudden jumps
                while (deltaX != 0 || deltaY != 0) {
                    int moveX = constrain(deltaX, -128, 127);  // Limit X movement to avoid overflow
                    int moveY = constrain(deltaY, -128, 127);  // Limit Y movement similarly
                    Mouse.move(moveX, moveY);  // Perform the mouse movement
                    deltaX -= moveX;  // Decrease remaining movement for X-axis
                    deltaY -= moveY;  // Decrease remaining movement for Y-axis
                }
            }
        }
        // Command: C - Mouse click (left button)
        else if (command.startsWith("C")) {
            // Initiate humanized click if not already clicking
            if (!isClicking) {
                Mouse.press(MOUSE_LEFT);  // Depress left button
                clickStartTime = millis();  // Record press timestamp
                clickDuration = random(40, 80);  // Randomize 40-80ms duration
                isClicking = true;  // Set active click flag
            }
        }
    }

    // Manage active click release timing
    if (isClicking) {
        // Check if click duration has elapsed
        if (millis() - clickStartTime >= clickDuration) {
            Mouse.release(MOUSE_LEFT);  // Release left button
            isClicking = false;  // Clear click flag
        }
    }
}

/*
 * DEOX Communication Protocol:
 * 
 * Commands (terminated with \n):
 *   M<x>,<y>  - Move mouse by x,y pixels
 *               Example: M10,-5 (move right 10, up 5)
 *   
 *   C         - Perform left click with randomized duration
 *               Humanized timing: 40-80ms hold
 * 
 * Movement Handling:
 *   - Accepts signed integers for deltaX, deltaY
 *   - Constrains moves to ±127 per iteration (HID limit)
 *   - Loops for large movements to prevent overflow
 * 
 * Notes:
 *   - All commands must end with newline (\n)
 *   - Invalid commands are silently ignored
 *   - No acknowledgment sent (fire-and-forget protocol)
 */