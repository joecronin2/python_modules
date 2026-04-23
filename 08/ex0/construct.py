import sys
import site


def environment_info():
    return {
        "in_venv": sys.prefix != sys.base_prefix,
        "python_executable": sys.executable,
        "prefix": sys.prefix,
        "base_prefix": sys.base_prefix,
        "site_packages": site.getsitepackages(),
    }


if __name__ == "__main__":
    for k, v in environment_info().items():
        print(f"{k}: {v}")

    if sys.prefix == sys.base_prefix:
        print("no venv detected...")
        print(" create one with 'python -m venv env_name'")
        print(" activate it with 'source ./env_name/bin/activate'")
