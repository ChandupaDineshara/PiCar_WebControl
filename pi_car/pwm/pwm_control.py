import os, time

os.system("sudo pkill -f generate_pwm.py")
print("stopped !!!")

#time.sleep(0.1)

print("starting pwm")
os.system("python /var/www/html/pi_car/pwm/generate_pwm.py &")
print("started !!!")
