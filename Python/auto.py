import wpilib
import math
### Import the drivetrain class here
# import drivetrain


class Basic_Auto(wpilib.command.Command):
    def constructor(self, distance, speed):
        self.distance = distance
        self.speed = speed
        self.start_distance = 0
        
        ## Requires the drivetrain
        # requires(drivetrain)
        
    def initialize():
        ## Get the current encoder values
        # self.start_distance = drivetrain.encoder
    
    def execute():
        # Move the drivetrain at designated speed
        # drivetrain.move(speed, speed)
    
    def isFinished():
        # return math.abs(drivetrain.encoder) >= math.abs(distance)
    
    def end():
        # drivetrain.move(0, 0)
    