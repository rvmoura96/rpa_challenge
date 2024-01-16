# Technical specifications


The dependencies manager used on this project is [Poetry](https://python-poetry.org/). It's suggested to install the projects dependencies using it, this way you can run the automation easyly.

* It was developed with Python 3.10.6.

* And is required at least Python on version 3.10.

For the stack used is [BS4](https://beautiful-soup-4.readthedocs.io/en/latest/) supported by [HTTPX](https://www.python-httpx.org/).


# How to run
First, clone this repository using the following command:

```
git clone https://github.com/rvmoura96/rpa_challenge.git
```

Then enter into the project directory:
```
cd rpa_challenge
```

All the instructions to run is assuming that you have Poetry installed and you are on rpa_challenge directory


On the inthegration_tests directory run this command to install all the projects dependencies:
```
poetry install
```

After the installation run this command to activate a virtual environment where the projects dependencies were installed on the above instruction.
```
poetry shell
```

To run the automation use:
```
python automation.py
```
