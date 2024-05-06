import pathlib
import subprocess

# Define input and output folders
input_folder = pathlib.Path("calcium_data")
output_folder = pathlib.Path("calcium_processed")

# Create the output folder if it doesn't exist
output_folder.mkdir(parents=True, exist_ok=True)

# Activate Conda environment
conda_activate_command = "conda activate caiman && "
#source_command = "source ~/.bashrc && "  # Adjust if using different shell configuration file

# Iterate over each file in the input folder
for img_fpath in input_folder.glob("*ome.tif"):
    # Process the image using the Python script within the Conda environment
    output_file = output_folder / img_fpath.name
    subprocess.run(
        f" {conda_activate_command} python process_files.py {img_fpath} {output_file}",
        shell=True
    )
    print(f"Processed {img_fpath.name} and saved as {output_file}")
