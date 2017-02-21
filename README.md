
Bad Boids:

The Bad Boids library allows one to simulate flocking birds with a number of adjustable dynamic parameters.

Installation:

The library can be installed like any other standard PIP library. To install,

1)Download library
2)Navigate to 'setup.py' file
3)Execute using 'python setup.py install' (prefixing with sudo if required)
The library should now be installed on your system.

Usage:

The library can be called with 'badboids'. It will look for a configuration file in the current working directory named 'config.cfg', a different file location can be specified with the --config / -c option. The configuration file should contain at least the 4 parameter headers ([Boids], [Axis], [Animation], [Dynamics]). An example config.cfg with the default values can be found in this repository. If no config file is present then the simulation will execute with default values. An example call could be,

'badboids --config my_config.cfg'
The result should be animation of the flocking birds plotted using matplotlib.


Configuration Parameters:

Section - boidp

1)count: Number of birds. Default: 50
2)position_limits: Initial position limits. Format: [x_min, y_min, x_max, y_max] Default: [-450, 300, 50, 600]
3)velocity_limits: Initial velocity limits. Format: [x_min, y_min, x_max, y_max] Default: [0, -20, 10, 20]
            
Section - Axis

1)xlim: Plot X axis limits. Format: [x_min, x_max] Default: [-500, 1500]
2)ylim: Plot Y axis limits. Format: [x_min, x_max] Default: [-500, 1500]

Section - Animation

1)frames: Total frames in animation. Default: 50
2)interval: Time between frames. Default: 50 
        
Section - Dynamics

1)move_to_middle_strength: Tendency for birds to move to flock center. Default: 0.01
2)alert_distance: Maximum distance to other bird for it to be considered for move to middle force. Default: 100
3)formation_flying_strength: Tendency for birds to not get too close to each other. Default: 0.125
4)formation_flying_distance: Maximum distance to other bird for it to be considered for formation force. Default: 10000
        
    Writing README.md