import math
import numpy
import scipy.misc


class Heatmap:
    def __init__(self, height=600, width=1200):
        self.map = numpy.zeros((height, width), dtype=numpy.int16)
        self.height = height
        self.width = width

    def add_point(self, lat, long, weight=1, radius=0):
        """
        add point to map
        :param lat:
        :param long:
        :param weight:
        :param radius:
        :return:
        """
        lat = float(lat)
        long = float(long)

        if abs(lat) > 90 or abs(long) > 180:
            return False

        x = (long + 180) * (self.width / 360)

        mercator = math.log(math.tan((math.pi / 4) + (math.radians(lat) / 2)))
        y = (self.height / 2) - (self.width * mercator / (2 * math.pi))

        try:
            if radius == 0:
                self.map[y][x] += 1 - int(self.map[y][x] - self.map[y][x] / 2)
            else:
                a, b = y, x
                y, x = numpy.ogrid[-a:self.height - a, -b:self.width - b]
                self.map[x ** 2 + y ** 2 <= radius ** 2] += weight
            return True
        except:
            return False

    def save(self, file):
        """
        render and export map to image file
        :param file:
        """
        scipy.misc.imsave(file, self.map)
