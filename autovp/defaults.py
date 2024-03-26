# ===================================================================== #
#  File name:      defaults.py                                          #
#  Author:         Arjan Lemmens                                        #
#  Date:           26-Mar-2023                                          #
#  Description:    Place for global definitions                         #
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
from dataclasses import dataclass

@dataclass
class _Arch:
    RISCV64: str = "riscv64"
    RISCV32: str = "riscv32"
    L_VALID_ARCH:list = ["riscv64", "riscv32"]
    
ARCH = _Arch()