import os
import subprocess
import platform


def deleteusb():
    name = subprocess.check_output(["whoami"], text=True).strip()
    print(name)
    paths = f"../../run/media/{name}/"
    result = subprocess.check_output(["ls", paths], text=True)
    nameofusb = result.strip()
    paths += nameofusb
    print(paths)
    for file in os.listdir(paths):
        # deletes only file
        # if os.path.isfile(f"{paths}/{file}"):
        #     os.system(f"rm {paths}/{file}")
        #     print(f"{file} deleted sucessfully!")

        # deletes everything that starts with day
        if file.startswith("day"):
            os.system(f"rm -rf {paths}/{file}")
            print(f"{file} deleted sucessfully!")


def is_device_mounted(device):
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
    if not is_device_mounted(device):
        print(f"{device} is not mounted, mounting now...")
        os.system(f"udisksctl mount -b {device}")


current_os = platform.system()


if current_os == "Linux":
    device = "/dev/sda1"
    mount_device(device)
    deleteusb()  # to delte contents in usb drive
