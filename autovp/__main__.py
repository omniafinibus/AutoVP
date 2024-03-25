# ===================================================================== #
#  File name:      __main__.py                                          #    
#  Author:         Arjan Lemmens                                        #
#  Date:           25-Mar-2023                                          #
#  Description:    Main file for the automatic virtual prototype        #
#                  generator.                                           #        
#  Rev:            2.1                                                  #
#                                                                       #
#                                                                       #
#                                                                       #
# ===================================================================== #
#  Revision history:                                                    #
#  Date        Description                                              #
#  25-Mar-2023 File created                                             #
# ===================================================================== #
#  To-Do: !=Priority, ~=Bug, ?=Idea/nice to have                        #
#                                                                       #
# ===================================================================== #

# =========== #
#   Imports   #
# =========== #
import logging
from log import setup_custom_logger

# ============== #
#   Definition   #
# ============== #
GOODBYE = False

# ============= #
#   Variables   #
# ============= #
gLogger = setup_custom_logger('root', '../logs/', True, logging.DEBUG)

# ============= #
#   Functions   #
# ============= #
def hello_world(hello:bool = True):
    if hello:
        print("Hello world")
        return
    print("Goodbye")

# ======================== # Main Code # ======================== #
logging.info(f"Printing \"hello world\"")
hello_world()
hello_world(GOODBYE)