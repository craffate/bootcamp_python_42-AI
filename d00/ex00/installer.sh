#!/bin/bash

PYTHON_PATH="/goinfre/miniconda"
PYTHON_EXEC="$PYTHON_PATH/bin/python"

remove_python()
{
	rm -rf $PYTHON_PATH
	echo "Python has been removed."
}

install_python()
{
	curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -o ./miniconda.sh
	zsh ./miniconda.sh -b -p $PYTHON_PATH
	rm ./miniconda.sh
	echo "Python has been installed."
}

case $1 in
	install-python)
		if [ -f $PYTHON_EXEC ]; then
			echo -e "Python is already installed, do you want to reinstall it?"
			read -p "[yes|no]> " INPUT
			if [ $INPUT == "yes" ]; then
				remove_python
				install_python
			else
				echo "exit."
				exit
			fi
		else
			install_python
		fi
		;;
	remove-python)
		remove_python
		;;
	*)
		echo "Usage: ./installer.sh [install-python  | remove-python]"
		;;
esac
