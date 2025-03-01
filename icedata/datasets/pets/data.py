__all__ = ["NUM_CLASSES", "class_map", "load_data", "load"]

from icevision.imports import *
from icevision.core import *
from icevision.utils import *


_CLASSES = sorted(
    {
        "Abyssinian",
        "great_pyrenees",
        "Bombay",
        "Persian",
        "samoyed",
        "Maine_Coon",
        "havanese",
        "beagle",
        "yorkshire_terrier",
        "pomeranian",
        "scottish_terrier",
        "saint_bernard",
        "Siamese",
        "chihuahua",
        "Birman",
        "american_pit_bull_terrier",
        "miniature_pinscher",
        "japanese_chin",
        "British_Shorthair",
        "Bengal",
        "Russian_Blue",
        "newfoundland",
        "wheaten_terrier",
        "Ragdoll",
        "leonberger",
        "english_cocker_spaniel",
        "english_setter",
        "staffordshire_bull_terrier",
        "german_shorthaired",
        "Egyptian_Mau",
        "boxer",
        "shiba_inu",
        "keeshond",
        "pug",
        "american_bulldog",
        "basset_hound",
        "Sphynx",
    }
)
NUM_CLASSES = len(_CLASSES) + 1


def class_map(background: int = "background"):
    return ClassMap(classes=_CLASSES, background=background)


def load_data(force_download: bool = False):
    base_url = "http://www.robots.ox.ac.uk/~vgg/data/pets/data"
    save_dir = get_data_dir() / "pets"
    save_dir.mkdir(exist_ok=True)

    url_images = os.path.join(base_url, "images.tar.gz")
    images_tar_file = save_dir / "images.tar.gz"
    if not images_tar_file.exists() or force_download:
        download_and_extract(url=url_images, save_path=images_tar_file)

    annotations_tar_file = save_dir / "annotations.tar.gz"
    if not annotations_tar_file.exists() or force_download:
        url_annotations = os.path.join(base_url, "annotations.tar.gz")
        download_and_extract(url=url_annotations, save_path=annotations_tar_file)

    return save_dir


def load(force_download: bool = False):
    warnings.warn("load will be deprecated in 0.1.0, please use load_data instead")
    return load_data(force_download=force_download)
