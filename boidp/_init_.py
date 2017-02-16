
from boidp import boids
from matplotlib import pyplot as plt
from argparse import ArgumentParser
import ConfigParser
import json

def main():

    parser = ArgumentParser(description = "Simulation of flocking birds")
    parser.add_argument('--config', '-c', help = 'Config file', default='config.cfg')
    args = parser.parse_args()

    try:
        defaults = {
            'count': '50',
            'position_limits': '[-450, 300, 50, 600]',
            'velocity_limits': '[0, -20, 10, 20]',

            'xlim': '[-500, 1500]',
            'ylim': '[-500, 1500]',

            'frames'  : '50',
            'interval': '50',

            'move_to_middle_strength': '0.01',
            'alert_distance': '100',
            'formation_flying_distance': '10000',
            'formation_flying_strength': '0.125'
        }

        config = ConfigParser.SafeConfigParser(defaults)
        with open(args.config) as f:
            config.readfp(f)

            count = config.getint('Boids', 'count')
            position_limits =  json.loads(config.get('Boids', 'position_limits'))
            velocity_limits =  json.loads(config.get('Boids', 'velocity_limits'))
            frames = config.getint('Animation', 'frames')
            interval = config.getint('Animation', 'interval')
            xlim = json.loads(config.get('Axis', 'xlim'))
            ylim = json.loads(config.get('Axis', 'ylim'))
            move_to_middle_strength = config.getfloat('Dynamics', 'move_to_middle_strength')
            alert_distance = config.getfloat('Dynamics', 'alert_distance')
            formation_flying_distance = config.getfloat('Dynamics', 'formation_flying_distance')
            formation_flying_strength = config.getfloat('Dynamics', 'formation_flying_strength')

            boid = boids(boid_count = count,
                         position_limits = position_limits,
                         velocity_limits = velocity_limits,
                         move_to_middle_strength = move_to_middle_strength,
                         alert_distance = alert_distance,
                         formation_flying_distance = formation_flying_distance,
                         formation_flying_strength = formation_flying_strength)
            boid.simulate(frames = frames,
                          interval = interval,
                          xlim = tuple(xlim),
                          ylim = tuple(ylim))
    except IOError as e:
        print 'Warning: Config file not found. Default: config.cfg. Can be changed with option --config'
        print 'Running with default values.'
        boid = boids()
        boid.simulate()
    except ConfigParser.NoSectionError as e:
        print 'Warning: Invalid config file. Make sure all sections ([Boids], [Axis], [Animation], [Dynamics]) are present.'
        print e
        print 'Running with default values.'
        boid = boids()
        boid.simulate()
        
Writing _init_.py