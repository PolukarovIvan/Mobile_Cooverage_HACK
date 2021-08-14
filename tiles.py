import numpy as np


class GlobalPixelCoordinates(object):

    def __init__(self):
        self.ecs = 0.0818191908426

    def calc_beta(self, latitude):
        return np.pi * latitude / 180

    def calc_phi(self, latitude):
        beta = self.calc_beta(latitude)
        return (1 - self.ecs * np.sin(beta)) / (1 + self.ecs * np.sin(beta))

    def calc_teta(self, latitude):
        beta = self.calc_beta(latitude)
        phi = self.calc_phi(latitude)

        return np.tan(np.pi / 4 + beta / 2) * np.power(phi, self.ecs / 2)

    def calc_rho(self, z):
        return np.power(2, z + 8) / 2

    def calc_x_y(self, latitude, longitude, z):
        teta = self.calc_teta(latitude)
        rho = self.calc_rho(z)

        return (rho * (1 + longitude / 180) / 256).astype(int), \
               (rho * (1 - np.log(teta) / np.pi) / 256).astype(int)


if __name__ == '__main__':
    print(GlobalPixelCoordinates().calc_x_y(*map(float, input().split(', '))))
