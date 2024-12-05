import subprocess


def get_usb_device():
    """Get the USB device path based on 'lsblk' output."""
    try:
        # List all block devices with their mount points
        result = subprocess.check_output(["lsblk", "-o", "NAME,MOUNTPOINT"], text=True)
        # Split the result into lines
        devices = result.strip().splitlines()

        for device in devices:
            # If the device has no mount point, it might be a USB device
            print(device)
            if "usb" in device.lower() and "mountpoint" not in device:
                # Get the device name (e.g., sdb1, sdc1, etc.)
                device_name = device.split()[0]
                device_path = f"/dev/{device_name}"
                return device_path
    except subprocess.CalledProcessError as e:
        print(f"Error checking block devices: {e}")
    return None


def mount_device(device):
    """Mount the device only if it isn't mounted."""
    try:
        # Run the mount command with sudo
        subprocess.run(["sudo", "udisksctl", "mount", "-b", device], check=True)
        print(f"{device} mounted successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error mounting {device}: {e}")


# Get USB device dynamically
usb_device = get_usb_device()

if usb_device:
    mount_device(usb_device)
else:
    print("No USB device found.")
