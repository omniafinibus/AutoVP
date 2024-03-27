# ===================================================================== #
#  File name:      VirtualPrototype.py                                  #
#  Author:         Arjan Lemmens                                        #
#  Date:           25-Mar-2023                                          #
#  Description:    File containing the class which encompasses the full #
#                  virtual prototype                                    #
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
from module import Core
from ..defaults import ARCH

class VirtualPrototype:
    
    def __init__(self, name:str) -> None:
        """Class holding all info of the virtual protoype

        :param name: Name of the virtual prototype
        :type name: str
        """        
        self._lCores = list()
        """List of all cores of the virtual prototype"""
        self._arch = ARCH.RISCV64
        """Arhcitecture type"""
        self._name = name
        
    @property
    def name(self):
        """Name of the module, this will be used as variable name"""
        return self._name

    @name.setter
    def name(self, value):
        logging.info(f"Property \"name\" of {self.name} has been set to {value}")
        self._name = value

    @name.deleter
    def name(self):
        logging.info(f"Property \"name\" of {self.name} has been deleted.")
        del self._name

    def add_core(self):
        """add_core to this virtual prototype"""        
        logging.info(f"A core has been added to the VP: {self.name}. Making the total amount of cores {len(self._lCores) + 1}")
        self._lCores.append(Core(len(self._lCores)))
    
    def get_core(self, id:int):
        """get_core Get a core based on its ID

        :param id: ID of the core to retrieve
        :type id: int
        :return: Core with the matching ID
        :rtype: Core or None on fail
        """        
        for core in self._lCores:
            if core.id == id:
                return core                
        return None
        
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
