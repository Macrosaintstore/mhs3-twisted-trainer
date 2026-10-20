import time
from typing import Optional

import pymem
import pymem.process


class GameProcess:
    """Wraps pymem for the MHS3 game process."""

    def __init__(self, exe_name: str):
        self.exe_name = exe_name
        self.pm: Optional[pymem.Pymem] = None
        self.base: int = 0

    def attach(self) -> bool:
        try:
            self.pm = pymem.Pymem(self.exe_name)
            module = pymem.process.module_from_name(self.pm.process_handle, self.exe_name)
            if module is None:
                return False
            self.base = module.lpBaseOfDll
            return True
        except pymem.exception.ProcessNotFound:
            return False

    def read_int(self, address: int) -> int:
        if self.pm is None:
            raise RuntimeError("not attached")
        return self.pm.read_int(address)

    def write_int(self, address: int, value: int) -> None:
        if self.pm is None:
            raise RuntimeError("not attached")
        self.pm.write_int(address, value)

    def wait_for_exit(self, poll: float = 1.0) -> None:
        while self.pm is not None and self.pm.process_handle:
            time.sleep(poll)
            try:
                self.read_int(self.base)
            except Exception:
                return