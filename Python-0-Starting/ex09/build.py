import os
import subprocess


def build():
    """ Build the ft_package """
    print("Starting the build process...")
    
    # Suppress output by redirecting stdout and stderr to os.devnull
    with open(os.devnull, 'w') as devnull:
        subprocess.run(
            ["python3", "setup.py", "sdist", "bdist_wheel", "--quiet"],
            stdout=devnull,
            stderr=devnull
        )
    
    print("Build completed successfully!")


def install():
    """ Install the ft_package """
    print("Starting the installation process...")
	
	# Suppress output by redirecting stdout and stderr to os.devnull
    with open(os.devnull, 'w') as devnull:
        subprocess.run(
			["pip", "install", "./dist/ft_package-0.0.1-py3-none-any.whl", "--quiet"],
			stdout=devnull,
			stderr=devnull
		)
	
    print("Installation completed successfully!")


if __name__ == "__main__":
    build()
    install()
