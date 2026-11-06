import sys

from image import Image, ImageError


class Binary_Image(Image):
    """
    An extended Image class that supports parsing binary PGM files.
    """

    @classmethod
    def read_pgm_binary(cls, filename):
        with open(filename, "rb") as f:
            lines = f.readlines()
            (magic, size, max) = (x.decode()[:-1] for x in lines[:3])
            if magic != "P5":
                raise ImageError("unrecognized magic number")

        image = Binary_Image()
        image.width, image.height = (int(x) for x in size.split(" "))
        image.max_value = int(max)

        image.pixels  = list(map(int, lines[3]))

        return image

    @classmethod
    def from_image(cls, image : Image):
        bimage = cls.__new__(cls)
        bimage.__dict__.update(image.__dict__)
        return bimage

    def write_pgm_binary(self, filename):
        pass
