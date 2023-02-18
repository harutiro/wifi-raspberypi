
import py_qmc5883l
sensor = py_qmc5883l.QMC5883L()
sensor.calibration = [
    [ 1.13686028e+00, -8.51865926e-02, -1.00508939e+03],
    [-8.51865926e-02,  1.05302309e+00,  5.98478850e+03],
    [ 0.00000000e+00,  0.00000000e+00,  1.00000000e+00]
]
# m = sensor.get_magnet()

while True:
    m = sensor.get_bearing()
    print(m)