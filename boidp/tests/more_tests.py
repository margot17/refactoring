
from nose.tools import assert_raises, assert_equal
from ..boids import Boids
import os
import yaml
import numpy as np
from numpy import testing as npTest
from mock import Mock, patch

# Test the new_flock(self, count, lower_limits, upper_limits) function
def test_new_flock():
    with open(os.path.join(os.path.dirname(__file__),'fixtures', 'samples_new_flock_unit.yaml')) as fixtures_file:
        fixtures = yaml.load(fixtures_file)
        for fixture in fixtures:
            rand       = fixture.pop('rand')
            positions  = fixture.pop('positions')
            velocities = fixture.pop('velocities')
            with patch.object(np.random, 'rand', return_value=rand) as mock_method:
                boids = Boids()
                npTest.assert_array_equal(np.asarray(positions),  boids.positions)
                npTest.assert_array_equal(np.asarray(velocities), boids.velocities)
                
                # Test the update_boids(self, positions, velocities) function
def test_update_boids():
    with open(os.path.join(os.path.dirname(__file__),'fixtures', 'samples_update_boids_unit.yaml')) as fixtures_file:
        fixtures = yaml.load(fixtures_file)
        for fixture in fixtures:
            before = fixture.pop('before')
            after  = fixture.pop('after')
            boids = Boids()
            boids.positions  = np.array(before[0:2])
            boids.velocities = np.array(before[2:4])
            boids.update_boids(boids.positions, boids.velocities)
            npTest.assert_array_almost_equal(boids.positions , np.array(after[0:2]))
            npTest.assert_array_almost_equal(boids.velocities, np.array(after[2:4]))

            # Test the separations_square_distances(self, positions) function
def test_separations_square_distances():
    with open(os.path.join(os.path.dirname(__file__),'fixtures', 'samples_separation_square_distances_unit.yaml')) as fixtures_file:
        fixtures = yaml.load(fixtures_file)
        for fixture in fixtures:
            positions        = fixture.pop('positions')
            fix_square_distances = fixture.pop('square_distances')
            fix_separations      = fixture.pop('separations')
            boids = Boids()
            boids.positions  = np.array(positions)
            separations, square_distances = boids.separations_square_distances(boids.positions)
            npTest.assert_array_almost_equal(separations[0][0] , np.array(fix_separations)[0])

            # Test the fly_towards_middle(self, positions, velocities) function
def test_fly_towards_middle():
    with open(os.path.join(os.path.dirname(__file__),'fixtures', 'samples_fly_towards_middle_unit.yaml')) as fixtures_file:
        fixtures = yaml.load(fixtures_file)
        for fixture in fixtures:
            before = fixture.pop('before')
            after  = fixture.pop('after')
            boids = Boids()
            boids.positions  = np.array(before[0:2])
            boids.velocities = np.array(before[2:4])
            boids.fly_towards_middle(boids.positions, boids.velocities)
            npTest.assert_array_almost_equal(boids.positions , np.array(after[0:2]))
            npTest.assert_array_almost_equal(boids.velocities, np.array(after[2:4]))
            
            # Test the fly_away_from_nearby_boids(self, positions, velocities, separations, square_distances)
def test_fly_away_from_nearby_boids():
    with open(os.path.join(os.path.dirname(__file__),'fixtures', 'samples_fly_away_from_nearby_boids_unit.yaml')) as fixtures_file:
        fixtures = yaml.load(fixtures_file)
        for fixture in fixtures:
            before = fixture.pop('before')
            after  = fixture.pop('after')
            boids = Boids()
            boids.positions  = np.array(before[0:2])
            boids.velocities = np.array(before[2:4])
            separations, square_distances = boids.separations_square_distances(boids.positions)
            boids.fly_away_from_nearby_boids(boids.positions, boids.velocities, separations, square_distances)
            npTest.assert_array_almost_equal(boids.positions , np.array(after[0:2]))
            npTest.assert_array_almost_equal(boids.velocities, np.array(after[2:4]))
            
            # Test the match_speed_with_nearby_birds(self, positions, velocities, square_distances) function
def test_match_speed_with_nearby_birds():
    with open(os.path.join(os.path.dirname(__file__),'fixtures', 'samples_match_speed_with_nearby_birds_unit.yaml')) as fixtures_file:
        fixtures = yaml.load(fixtures_file)
        for fixture in fixtures:
            before = fixture.pop('before')
            after  = fixture.pop('after')
            boids = Boids()
            boids.positions  = np.array(before[0:2])
            boids.velocities = np.array(before[2:4])
            separations, square_distances = boids.separations_square_distances(boids.positions)
            boids.match_speed_with_nearby_birds(boids.positions, boids.velocities, square_distances)
            npTest.assert_array_almost_equal(boids.positions , np.array(after[0:2]))
            npTest.assert_array_almost_equal(boids.velocities, np.array(after[2:4]))


Writing more_tests.py