import h5py

# Path to your .h5 file
file_path = 'fpn_inception.h5'

# Open the .h5 file
with h5py.File(file_path, 'r') as file:
    # Print the structure of the file
    def print_structure(name, obj):
        if isinstance(obj, h5py.Dataset):
            print(f"Dataset: {name}, Shape: {obj.shape}, Dtype: {obj.dtype}")
        elif isinstance(obj, h5py.Group):
            print(f"Group: {name}")

    file.visititems(print_structure)

    # Access specific datasets or groups if needed
    # Example: data = file['dataset_name'][:]
