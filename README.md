# pywebview-react-boilerplate
_pywebview_ lets you build GUI for your Python program with JavaScript, HTML, and CSS. This is a  simple boilerplate to help you start with pywebview and React. It sets up the development environment, install dependencies, as well as provides scripts for building an executable. Stack is based on pywebview, React, SASS, Parcel bundler, pyinstaller (Windows/Linux) and py2app (macOS).

## Requirements
- Python 3
- Node
- virtualenv

## Installation

``` bash
npm run init
```

This will create a virtual environment, install pip and Node dependencies. Alternatively you can perform these steps manually

``` bash
npm install
pip -r requirements.txt
```

On Linux systems installation system makes  educational guesses. If run under KDE, QT dependencies are installed, otherwise GTK is chosen. `apt` is used for installing GTK dependencies. If you are running a non apt-based system, then you will have to install GTK dependencies manually. Suggestions on how to improve installation on Linux are welcomed.

## Usage

To launch application

``` bash
npm run start
```

To build an executable. The output binary will be produced in the `dist` directory.

``` bash
npm run build
```

To start a development server (only for testing frontend code)

``` bash
npm run dev
```


## Bug reporting

Please report _pywebview_ related bugs directly to [pywebview's repository](https://github.com/r0x0r/pywebview). This repository is only for the issues related to this boilerplate.