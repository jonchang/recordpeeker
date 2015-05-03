# Installing Record Peeker

## Mac OS X

*Note: Only tested on OS X Yosemite 10.0*

1.  Start up Terminal (`/Applications/Utilities/Terminal.app`).

2.  In Terminal, type in:

    ```
    xcode-select --install
    ```

    An alert box (similar to the one below) will pop up. Click "Install" to download and install Xcode.

    ![Xcode alert popup](http://railsapps.github.io/images/installing-mavericks-popup.png)

    (Note - if you are not using Yosemite you will probably have to download Xcode from [Apple's Developer site.](https://developer.apple.com/xcode/)

3.  Install [Homebrew](http://brew.sh/). Type into your Terminal:

    ```
    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    ```

    You may have to enter your password.

4.  Install Python.

    ```
    brew install python
    ```

5.  Install Record Peeker.

    ```
    pip install git+https://github.com/jonchang/recordpeeker.git
    ```

    If there are any updates, you can just run the above command again to pull down any updates.

## Windows

*Note: only tested on Windows 8.1*

1.  Install Python at https://www.python.org/downloads/release/python-279/ (use the MSI installer)

2.  Add Python to the beginning of your PATH variable.

    ```
    C:\Python27\;C:\Python27\Scripts\;
    ```

    There are [a number of ways to do this](https://www.google.com/search?q=windows+add+to+path); I press Windows Key-Break, then go to Advanced System Settings, Environment Variables.

3.  Download and run [`easy_install`](https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py). You should be able to double-click it to install it.

4.  Install `pip`. Open up your Command Prompt and type in:

    ```
    easy_install pip
    ```

    Note: at this step I had a Python cp65001 error. It's a simple issue to fix but the Python developers refuse to implement it for Python 2.7. I got around it by typing `set PYTHONIOENCODING=utf-8` into my command prompt.

5.  Install Record Peeker.

    ```
    pip install git+https://github.com/jonchang/recordpeeker.git
    ```

    If there are any updates, you can just run the above command again to pull down any updates.

## Linux

1.  Probably `apt-get install python-pip` followed by step 5 above. If you run Linux you should be able to figure this out on your own.
