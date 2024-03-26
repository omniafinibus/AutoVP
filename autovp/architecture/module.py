# ===================================================================== #
#  File name:      module.py                                            #
#  Author:         Arjan Lemmens                                        #
#  Date:           26-Mar-2023                                          #
#  Description:    File containing the class which describes a modular  #
#                  part of a vp                                         #
#  Rev:            0.1                                                  #
# ===================================================================== #
#  Revision history:                                                    #
#  Author   Date        Description                                     #
#  A.lem    26-Mar-2023 File created                                    #
# ===================================================================== #
#  To-Do: !=Priority, ~=Bug, ?=Idea/nice to have                        #
#                                                                       #
# ===================================================================== #

# =========== #
#   Imports   #
# =========== #
import logging

class Module:
    def __init__(self, name:str, sourceFile:str, addrSize:int, lDependencies:list = None):
        """Class containig all info on a single resource

        :param name: Name of the module as variable
        :type name: str
        :param sourceFile: Name of the cpp source file, to be used in the include header
        :type sourceFile: str
        :param addrSize: Amount of bytes the TLM bus will reserve for this module
        :type addrSize: int
        :param lDependencies: List of all dependencies need to be initialized before this module is initialized, defaults to None
        :type lDependencies: list, optional
        """
        self._name = name
        """Name of the module, this will be used as variable name"""
        self._sourceFile = sourceFile
        """Directory/name of the header file to be included"""
        self.lDependencies = lDependencies
        """List of all dependencies needed by this module"""
        self._addrSize = addrSize
        """Port width assigned to this module"""
        self._startAddr = 0x0
        """First port address assigned to this module"""
        self._stopAddr = 0x0 + addrSize
        """last port address assigned to this module"""
        self._priority = 0
        """Priority of this module when assigning ports and sockets, 0 is the highest priority"""
        

    @property
    def name(self):
        """Name of the module, this will be used as variable name"""
        return self._name

    @name.setter
    def name(self, value):
        logging.info(f"Property \"name\" of {self._name} has been set to {value}")
        self._name = value

    @name.deleter
    def name(self):
        logging.info(f"Property \"name\" of {self._name} has been deleted.")
        del self._name

    @property
    def sourceFile(self):
        """Directory/name of the header file to be included"""
        return self._sourceFile

    @sourceFile.setter
    def sourceFile(self, value):
        logging.info(f"Property \"sourceFile\" of {self._name} has been set to {value}")
        self._sourceFile = value

    @sourceFile.deleter
    def sourceFile(self):
        logging.info(f"Property \"sourceFile\" of {self._name} has been deleted.")
        del self._sourceFile

    @property
    def addrSize(self):
        """Port width assigned to this module"""
        return self._addrSize

    @addrSize.setter
    def addrSize(self, value):
        logging.info(f"Property \"addrSize\" of {self._name} has been set to {value}")
        self._addrSize = value

    @addrSize.deleter
    def addrSize(self):
        logging.info(f"Property \"addrSize\" of {self._name} has been deleted.")
        del self._addrSize

    @property
    def startAddr(self):
        """First port address assigned to this module"""
        return self._startAddr

    @startAddr.setter
    def startAddr(self, value):
        logging.info(f"Property \"startAddr\" of {self._name} has been set to {value}")
        self._startAddr = value

    @startAddr.deleter
    def startAddr(self):
        logging.info(f"Property \"startAddr\" of {self._name} has been deleted.")
        del self._startAddr

    @property
    def stopAddr(self):
        """last port address assigned to this module"""
        return self._stopAddr

    @stopAddr.setter
    def stopAddr(self, value):
        logging.info(f"Property \"stopAddr\" of {self._name} has been set to {value}")
        self._stopAddr = value

    @stopAddr.deleter
    def stopAddr(self):
        logging.info(f"Property \"stopAddr\" of {self._name} has been deleted.")
        del self._stopAddr

    @property
    def priority(self):
        """Priority of this module when assigning ports and sockets, 0 is the highest priority"""
        return self._priority

    @priority.setter
    def priority(self, value):
        logging.info(f"Property \"priority\" of {self._name} has been set to {value}")
        self._priority = value

    @priority.deleter
    def priority(self):
        logging.info(f"Property \"priority\" of {self._name} has been deleted.")
        del self._priority