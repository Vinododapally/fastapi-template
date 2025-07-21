import sys

import pytest

if __name__ == "__main__":
    # Add the app directory to the system path
   exit_code=pytest.main(["--html=report.html", "--self-contained-html"])
   if exit_code != 0:
       raise SystemExit(exit_code)
   sys.exit(exit_code)