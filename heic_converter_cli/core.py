"""
License: MIT License, see LICENSE for more details.

HEIC to TIFF converter
"""
import argparse
import pathlib

import pyheif
from PIL import Image

def convert_heic_to_tiff(input_path: pathlib.Path, output_path: pathlib.Path):
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    # read the HEIC file
    heif_file = pyheif.read(input_path)
    
    # generate an image
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
    )
    
    # save the image as no compression TIFF
    image.save(output_path, format="TIFF", compression="raw")
    
    print(f"Converted: {input_path} -> {output_path}")

def main():
    parser = argparse.ArgumentParser(description="HEIC to TIFF converter")
    parser.add_argument("input", type=pathlib.Path, help="Input HEIC file")
    parser.add_argument("output", type=pathlib.Path, help="Output TIFF file")
    args = parser.parse_args()
    
    convert_heic_to_tiff(args.input, args.output)


if __name__ == "__main__":
    main()

