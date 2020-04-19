import subprocess
import sys

# Install benedict if not available
try:
    print('Checking for python-benedict dependency')
    from benedict import benedict

except ImportError:
    print('python-benedict not installed, attempting to install')
    try:
        subprocess.call([sys.executable, "-m", "pip", "install", 'python-benedict'])
    except:
        pass
    try:
        subprocess.call([sys.executable, "-m", "pip3", "install", 'python-benedict'])
    except:
        pass
finally:
    try:
        from benedict import benedict
        print('python-benedict should now be installed, done')
        exit(0)
    except ImportError:
        print('python-benedict failed to install, PLS H3LP')
        exit(1)

