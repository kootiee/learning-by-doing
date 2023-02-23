import inspect
import sys
import importlib.util

def main(module_path):
    spec = importlib.util.spec_from_file_location("target", module_path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["target"] = mod
    spec.loader.exec_module(mod)
    functions = inspect.getmembers(mod, inspect.isfunction)
    for name, fn in functions:
        # subtract 1 to account for the "def" line (yes, it's a hack)
        print(f"{name}: {len(inspect.getsourcelines(fn)[0])-1}")

if __name__ == '__main__':
    main(sys.argv[1])
