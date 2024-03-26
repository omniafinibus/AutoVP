# ===================================================================== #
#  File name:      base.py                                              #
#  Author:         Arjan Lemmens                                        #
#  Date:           25-Mar-2023                                          #
#  Description:    File containing the class which encompasses the full #
#                  RISC-V architecture                                  #
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
from module import Module
from ..defaults import ARCH

class RiscVArch:
    
    def __init__(self, lModules: list[Module]) -> None:
        """Class holding all info of the virtual protoype

        :param lModules: List of all modules present in the architecture
        :type lModules: list[Module]
        """        
        self.lModules = lModules
        """List of all modules present in the architecture"""
        self._arch = ARCH.RISCV64
        """Arhcitecture type"""
        
    @property
    def arch(self):
        """Arhcitecture type"""
        return self._arch

    @arch.setter
    def arch(self, value):
        if value not in ARCH.L_VALID_ARCH:
            logging.warning(f"Unknown architecture: {value}")
            return
        logging.info(f"Architecure change from {self._arch} too {value}")
        self._arch = value
