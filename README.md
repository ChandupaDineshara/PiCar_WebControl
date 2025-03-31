<h1 >PiCar: Web-Controlled Robot</h1>

<p>
  <img src="pi_car/IMG_20250401_014844_edit_786369379269064.jpg" alt="PiCar" width="50%" />
</p>

## Features

- **Web Interface**: Control the robot's movement (forward, backward, left, right, stop) using direction buttons.
- **Speed Control**: Adjust the motor speed with a slider.
- **Real-time Feedback**: Changes in direction and speed are applied instantly.

## Project Files

- `remote.php`: Web interface for robot control.
- `ajax_direction.php`: Handles direction commands from the interface.
- `ajax_speed.php`: Handles speed adjustment commands.
- `generate_pwm.py`: Python script to control the motors with PWM signals.
- `pwm_control.py`: Manages the PWM updates and ensures instant speed changes.
- `remote.css`: Styles the web interface for a better user experience.

## Setup Instructions

### Hardware Requirements:

- Raspberry Pi (any model with GPIO pins)
- Motor driver (e.g., L298N)
- Motors and wheels for movement
- Power supply for Raspberry Pi and motors

### Software Requirements:

- Python 3.x
- Apache2 (Web Server for PHP)
- PHP 7.x or above
- GPIO library for Raspberry Pi

## Install Dependencies:

Make sure you have PHP and a web server installed:

<pre><code>sudo apt-get update
sudo apt-get install apache2 php libapache2-mod-php
sudo apt-get install python3-rpi.gpio</code></pre>

You may also need to enable Apache to handle the PHP scripts:

<pre><code>sudo systemctl enable apache2</code></pre>

## Run the Web Server:

Make sure the Apache web server is running, then place the files in the server's root directory (e.g., `/var/www/html`):

<pre><code>sudo cp -r * /var/www/html/</code></pre>

After copying the files, restart the Apache server to apply the changes:

<pre><code>sudo systemctl restart apache2</code></pre>

Now, navigate to the Pi's IP address from a browser (`http://<RaspberryPi_IP>/remote.php`) to interact with the web interface.

