import os
import tkinter as tk
from tkinter import filedialog

def is_dds_file(file_path):
    # Checks if DDS
    with open(file_path, 'rb') as file:
        header = file.read(4)

    if header != b'DDS ':
        return False

    # Checks for Nvidia DDS signature
    with open(file_path, 'rb') as file:
        file.seek(0x44)
        signature = file.read(3)

    return signature == b'NVT'

def replace_block_with_zeros(file_path):
    try:
        if not is_dds_file(file_path):
            print(f"Skipping {file_path}: Not a valid NVIDIA DDS file.")
            return

        with open(file_path, 'rb') as file:
            data = bytearray(file.read())

        # Defines start and end indices to be nulled
        start_index = 0x44
        end_index = 0x48

        for i in range(start_index, end_index):
            data[i] = 0x00

        # Writes the modified data back to the file
        with open(file_path, 'wb') as file:
            file.write(data)

    except Exception as e:
        print(f"An error occurred while processing {file_path}: {e}")

def process_dds_files(file_paths):
    skipped_files = 0

    for file_path in file_paths:
        print(f"Checking {file_path}...")
        if is_dds_file(file_path):
            replace_block_with_zeros(file_path)
        else:
            print(f"Skipping {file_path}: Not a valid NVIDIA DDS file.")
            skipped_files += 1

    if skipped_files == len(file_paths):
        print("\nEpic fail!")
    elif skipped_files == 0:
        print("\nAll DDS files processed successfully!")
    else:
        print(f"\nDDS files processed successfully! ({skipped_files} {'file' if skipped_files == 1 else 'files'} skipped)")

# Tool info
print("DDS Impression Clearing Kit (D.I.C.K.) by 2VE")
print('Removes Nvidia Texture Tools Exporter\'s "NVTx" signature from the DDS file header.\n')

# Creates then hides Tkinter root window
root = tk.Tk()
root.withdraw()

# Asks to select DDS files
file_paths = filedialog.askopenfilenames(title="Select DDS files", filetypes=[("DDS files", "*.dds")])
if file_paths:
    process_dds_files(file_paths)
    input("Press enter to exit...")
