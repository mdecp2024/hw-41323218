# Given data
initial_velocity_kmh = 310  # initial velocity in km/h
distance = 1000  # distance in meters
 
# Convert initial velocity from km/h to m/s
initial_velocity_ms = initial_velocity_kmh * 1000 / 3600
 
# Final velocity (after stopping)
final_velocity = 0
 
# Using the equation v^2 = u^2 + 2as to solve for acceleration a
acceleration = (final_velocity**2 - initial_velocity_ms**2) / (2 * distance)
 
print(f"The required acceleration is {acceleration:.2f} m/s^2")
 