from Snapshot import Snapshot


class Snapshots:
    def __init__(self):
        self.snapshots_per_second = 0
        self.total_snapshots = 0
        self.snapshots_done = 0
        self.snapshots = []

    def addSnapshot(self, snapshot):
        snapshot.id = self.snapshots_done
        self.snapshots.append(snapshot)
        self.snapshots_done += 1

    def getSnapshot(self, i: int) -> Snapshot:
        return self.snapshots[i]

    def getLastSnapshot(self):
        return self.snapshots[self.snapshots_done - 1]

    def __str__(self) -> str:
        res = "Snapshots\n"
        res += "    Total snapshots: " + str(self.total_snapshots)
        res += "\n    Snapshots per second: " + str(self.snapshots_per_second)
        res += "\n    Snapshots done: " + str(self.snapshots_done) + "\n"

        for snapshot in self.snapshots:
            res += "\n   " + str(snapshot) + "\n"
        return res
