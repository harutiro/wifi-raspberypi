
import py_qmc5883l

class Compass:

    sensor = py_qmc5883l.QMC5883L()
    sensor.calibration = [
    [ 1.09902329e+00 , 6.60967065e-02 , 5.39201258e+03],
    [ 6.60967065e-02 , 1.04411866e+00 ,-2.20910689e+03],
    [ 0.00000000e+00 , 0.00000000e+00 , 1.00000000e+00]
]

    def get_bearing(self):
        return self.sensor.get_bearing()