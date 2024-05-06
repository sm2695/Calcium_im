import sys
import pathlib
from pyometiff import OMETIFFReader
import tifffile 

input_file = pathlib.Path(sys.argv[1])
output_folder = pathlib.Path(sys.argv[2])

reader = OMETIFFReader(fpath=input_file)
img_array, metadata, xml_metadata = reader.read()

output_file = output_folder / input_file.name
tifffile.imsave(output_file, img_array)

print(f"Processed {input_file.name} and saved as {output_file}")
