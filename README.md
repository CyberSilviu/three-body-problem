# three-body-problem

In this Python code, I'm simulating the gravitational interactions of three bodies, each with a mass (`m1`, `m2`, `m3`). I'm using the figure-eight initial conditions, where the bodies move in a specific pattern under the influence of gravity.

I define the gravitational constant `G` and set initial positions (`r1_0`, `r2_0`, `r3_0`) and velocities (`v1_0`, `v2_0`, `v3_0`) for each body. Time parameters (`T`, `dt`, `num_steps`) are specified for the simulation.

I create a function `calculate_acceleration` to compute the accelerations of each body based on their positions and masses. The initial conditions are flattened into a 1D array.

Using the `odeint` function from SciPy, I perform numerical integration to obtain the solution, which represents the positions of each body over time.

I set up the plot using Matplotlib, initializing positions and creating line objects for each body. Trail data is initialized for each body to visualize their paths, and an update function is defined for the animation.

The animation is created with `FuncAnimation`, and the resulting motion is displayed using Matplotlib. I also include a legend to label each body for better interpretation.
