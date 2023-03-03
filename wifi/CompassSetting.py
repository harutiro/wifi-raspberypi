
import py_qmc5883l

class Compass:

    sensor = py_qmc5883l.QMC5883L()
    sensor.calibration = [
        [ 1.13686028e+00, -8.51865926e-02, -1.00508939e+03],
        [-8.51865926e-02,  1.05302309e+00,  5.98478850e+03],
        [ 0.00000000e+00,  0.00000000e+00,  1.00000000e+00]
    ]

    def get_bearing(self):
        return self.sensor.get_bearing()