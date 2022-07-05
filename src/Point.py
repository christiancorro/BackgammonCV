from Color import Color


class Point:
    def __init__(self, id=0, center=(0, 0), bbox=[]):
        self.id = id
        self.center = center
        self.bbox = bbox
        self.bbox_warped = bbox
        self.disks = []
        self.color = Color.WHITE if (id % 2 == 0) else Color.BLACK

    def addDisk(self, disk):
        self.disks.append(disk)

    def reset(self):
        self.bbox_warped = self.bbox.copy()

    def clear(self):
        self.disks.clear()

    def __str__(self):
        res = ""
        res += str(self.id if self.id != 25 else "bar") + ":"  # + " (" + str(len(self.disks)) + "): "
        for disk in self.disks:
            res += str(disk)
        # res += "bbox: " + str(self.bbox)
        return res

    def copy(self):
        point = Point(self.id, self.center, self.bbox.copy())
        for disk in self.disks:
            newDisk = disk.copy()
            point.addDisk(newDisk)
        point.color = self.color

        return point
