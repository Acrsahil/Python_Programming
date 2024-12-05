import os
import subprocess

# os.system("ls")
#
# # print("***************************************")
# # print("***********Your are hacked*************")
# # print("***************************************")
#
#
# os.system("dolphin && exit")


def get_usb_partition():
    # Run lsblk to get block devices and their types
    result = subprocess.run(
        ["lsblk", "-lno", "NAME,RM,TYPE,MOUNTPOINT"], capture_output=True, text=True
    )

    lines = result.stdout.splitlines()

    # Search for removable disk (RM = 1)
    listofusb = []
    for line in lines:
        columns = line.split()
        print(columns)
        if len(columns) >= 3 and columns[1] == "1" and columns[0] not in listofusb and  columns[0].startswith(""):
        listofusb.append(f"columns[0]1")
        #     # Now find the partitions for this device
        #     return f"/dev/{device}1"  # Assuming it's a single partition USB drive

    return None


print(get_usb_partition())
