myVariable = 0

 

def when_started1():

global myVariable

motor_3.spin_for(REVERSE, 60, DEGREES)

motor_4.spin_for(FORWARD, 90, DEGREES)

drivetrain.drive_for(FORWARD, 350, MM)

motor_4.spin_for(REVERSE, 100, DEGREES)

brain.play_sound(SoundType.TADA)

drivetrain.drive_for(REVERSE, 400, MM)

drivetrain.turn_for(RIGHT, 181.5, DEGREES)

motor_3.spin_for(FORWARD, 75, DEGREES)

drivetrain.drive_for(FORWARD, 400, MM)

motor_4.spin_for(FORWARD, 90, DEGREES)

brain.play_sound(SoundType.TADA)

motor_3.spin_for(FORWARD, 75, DEGREES)

drivetrain.drive_for(REVERSE, 400, MM)

drivetrain.turn_for(RIGHT, 181, DEGREES)

drivetrain.drive_for(FORWARD, 425, MM)

motor_4.spin_for(REVERSE, 100, DEGREES)

brain.play_sound(SoundType.TADA)

drivetrain.drive_for(REVERSE, 400, MM)

drivetrain.turn_for(RIGHT, 180, DEGREES)

motor_3.spin_for(REVERSE, 100, DEGREES)

drivetrain.drive_for(FORWARD, 410, MM)

motor_4.spin_for(FORWARD, 90, DEGREES)

brain.play_sound(SoundType.TADA)

drivetrain.drive_for(REVERSE, 400, MM)

drivetrain.turn_for(RIGHT, 181.5, DEGREES)

drivetrain.drive_for(FORWARD, 450, MM)

motor_4.spin_for(REVERSE, 100, DEGREES)

brain.play_sound(SoundType.TADA)

drivetrain.drive_for(REVERSE, 400, MM)

drivetrain.turn_for(RIGHT, 181, DEGREES)

motor_3.spin_for(REVERSE, 103, DEGREES)

drivetrain.drive_for(FORWARD, 430, MM)

motor_4.spin_for(FORWARD, 90, DEGREES)

brain.play_sound(SoundType.TADA)

 

when_started1()
