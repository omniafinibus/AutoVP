# ===================================================================== #
#  File name:      __main__.py                                          #    
#  Author:         Arjan Lemmens                                        #
#  Date:           25-Mar-2023                                          #
#  Description:    Main file for the automatic virtual prototype        #
#                  generator.                                           #        
#  Rev:            0.1                                                  #
# ===================================================================== #
#  Revision history:                                                    #
#  Author   Date        Description                                     #
#  A.lem    25-Mar-2023 File created                                    #
# ===================================================================== #
#  To-Do: !=Priority, ~=Bug, ?=Idea/nice to have                        #
#                                                                       #
# ===================================================================== #

# =========== #
#   Imports   #
# =========== #
import logging
import argparse
from defaults import ARCH
from log import setup_custom_logger
from architecture import VirtualPrototype

# ============== #
#   Definition   #
# ============== #
GOODBYE = False

# ============= #
#   Variables   #
# ============= #
gLogger = setup_custom_logger('root', './logs/', True, logging.DEBUG)

# ============= #
#   Functions   #
# ============= #
def hello_world(hello:bool = True):
    if hello:
        print("Hello world")
        return
    print("Goodbye")

# ======================== # Main Code # ======================== #

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--mem", help="size of the memory", type=float)
parser.add_argument("-c", "--core_count", help="Number of cores present", type=int, choices=range(1,32), default=1)
args = parser.parse_args()

virtualProtoype = VirtualPrototype(list())

virtualProtoype.arch = ARCH.RISCV32


# Deploy directories and preliminary files

# Parse user inputs

# Fetch risc-v modules

# Order modules based on priorities (Important for module addresses)

# Update variables in modules

# Clean code?

# Create files

# Build vp

# Verify model