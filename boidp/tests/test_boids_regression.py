
from ..boidp import Boids
from nose.tools import assert_almost_equal
import os
import yaml
import numpy as np

def test_bad_boids_regression():
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures' ,'samples_boids_regression.yaml')))
    boid_data=np.array(regression_data["before"])
    boids = Boids()
    boids.update_boids(boid_data[0:2], boid_data[2:4])
    for after,before in zip(regression_data["after"],boid_data):
        for after_value,before_value in zip(after,before):
            assert_almost_equal(after_value,before_value,delta=0.01)
            
            Writing test_boids_regression.py