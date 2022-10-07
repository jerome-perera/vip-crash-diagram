import Lane

class Trajectory:
    def __init__(self, trajection_geometry):
        self.departing_lane = Lane()
        self.receiving_lane = Lane()
        self.trajection_geometry = trajection_geometry