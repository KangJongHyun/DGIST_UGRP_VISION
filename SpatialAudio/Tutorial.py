import numpy as np
import sounddevice as sd

duration = 5.0
sample_rate = 44100
t = np.linspace(0, duration, int(sample_rate * duration), False)

def generate_sound(frequency):
    note = np.sin(frequency * t * 2 * np.pi)
    note = note / np.max(np.abs(note))
    return note

def calculate_sound(distance, angle_radians, frequency):
    note = generate_sound(frequency)

    # Calculate the attenuation factor based on distance (assuming inverse square law)
    attenuation_factor = 1.0 / (distance ** 2)

    # Calculate the left and right volumes based on the angle (panning)
    left_volume = np.cos(angle_radians)  # Volume for the left channel
    right_volume = np.sin(angle_radians)  # Volume for the right channel

    # Apply the attenuation and panning to the sound signal
    left_sound = note * attenuation_factor * left_volume
    right_sound = note * attenuation_factor * right_volume

    # Combine the left and right sounds for stereo output
    audio_stereo = np.array([left_sound, right_sound])

    return audio_stereo

frequency = 440  # Hz (adjust this to change the pitch)

# Generate random distance and angle
distance = np.random.uniform(1, 10)  # Random distance between 1 and 10 meters
angle_degrees = np.random.uniform(0, 90)  # Random angle between 0 and 90 degrees

# Convert the angle from degrees to radians
angle_radians = np.radians(angle_degrees)

# Calculate the stereo sound
audio_stereo = calculate_sound(distance, angle_radians, frequency)

# Play the stereo sound using the default sound device
sd.play(audio_stereo.T, sample_rate, device=None)  # Set device to None for the default device
sd.wait()

# Ask the user to input their guess for distance and angle
user_distance = float(input("Enter your guess for the distance from the sound source (in meters): "))
user_angle_degrees = float(input("Enter your guess for the direction in degrees (0 to 90): "))

# Check the user's answer with a tolerance of 30% for distance and 30 degrees for angle
distance_tolerance = 0.3 * distance
angle_tolerance = 30

if abs(user_distance - distance) <= distance_tolerance and abs(user_angle_degrees - angle_degrees) <= angle_tolerance:
    print("Correct!")
else:
    print("Incorrect. The correct distance is {:.2f} meters and the correct angle is {:.2f} degrees.".format(distance, angle_degrees))
