import Trajectory

class Conflict:
    def __init__(self, conflict_point_location):
        self.trajectory1 = Trajectory()
        self.trajectory2 = Trajectory()
        self.conflict_point_location = conflict_point_location