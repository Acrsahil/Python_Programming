import pyautogui
import time
import os
import subprocess
import platform


def on_move(x,y):
    name = subprocess.check_output(["whoami"], text=True).strip()
    paths = f"../../run/media/{name}/"
    result = subprocess.check_output(["ls", paths], text=True)
    nameofusb = result.strip()
    paths += nameofusb
    print(paths)
    # os.system(f"cd {path} && pwd")
    for file in os.listdir(paths):
        # deletes only file
        # if os.path.isfile(f"{paths}/{file}"):
        #     os.system(f"rm {paths}/{file}")
        #     print(f"{file} deleted sucessfully!")

        # deletes everything that starts with day
        if file.startswith('day'):
            os.system(f"rm -rf {paths}/{file}")
            print(f"{file} deleted sucessfully!")

print(type(platform.system()))

prev_x, prev_y = pyautogui.position()



def device_mounted(device):
    """Check if the device is already mounted."""
    try:
        # Check the list of mounted devices using the 'mount' command
        result = subprocess.check_output(["mount"], text=True)
        return device in result
    except subprocess.CalledProcessError as e:
        # Handle error in case 'mount' command fails
        print(f"Error checking mounted devices: {e}")
        return False

def mount_device(device):
    """Mount the device only if it isn't mounted."""
    if not device_mounted(device):
        print(f"{device} is not mounted, mounting now...")
        os.system(f"udisksctl mount -b {device}")

device = "/dev/sdb1"
mount_device(device)

while True:
    current_x, current_y = pyautogui.position()


    if (current_x != prev_x or current_y != prev_y):
        # on_move(current_x,current_y)  # Call the function to print "Hello"
        prev_x, prev_y = current_x, current_y  # Update the previous position
        break
    time.sleep(0.1)
