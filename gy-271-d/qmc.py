
import py_qmc5883l
sensor = py_qmc5883l.QMC5883L()
sensor.calibration = [
    [ 1.09902329e+00 , 6.60967065e-02 , 5.39201258e+03],
    [ 6.60967065e-02 , 1.04411866e+00 ,-2.20910689e+03],
    [ 0.00000000e+00 , 0.00000000e+00 , 1.00000000e+00]
]
# m = sensor.get_magnet()

while True:
    m = sensor.get_bearing()
    print(m)