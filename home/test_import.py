# test_import.py
import sys, importlib, traceback
print("PYTHON:", sys.executable)
print("sys.path:")
for p in sys.path:
    print("  ", p)
try:
    importlib.import_module('django')
    print("django module file:", importlib.import_module('django').__file__)
    importlib.import_module('django.core.checks.urls')
    print("IMPORT_OK")
except Exception:
    traceback.print_exc()