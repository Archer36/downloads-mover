#!/usr/bin/env python3

import logging
from pathlib import Path

logging.basicConfig(level=logging.DEBUG)

downloads_directory = Path.home().joinpath("Downloads")
wallpaper_directory = Path.home().joinpath("Documents", "Wallpapers", "Mixed Resolutions")

if downloads_directory.exists():
    logging.debug("Downloads Directory Exists")

    images = sorted(downloads_directory.glob("*-unsplash.jpg"))

    logging.debug(f"List of wallpapers to be moved: {[image.name for image in images]}")

    if wallpaper_directory.exists():
        logging.debug("Destination wallpaper directory exists")
        for image in images:
            new_image_path = wallpaper_directory.joinpath(image.name)
            logging.debug(f"Moving: {new_image_path}")
            image.replace(new_image_path)
