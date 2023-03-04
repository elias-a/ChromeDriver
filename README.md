# ChromeDriver

A small wrapper around chromedriver that encapsulates common functionality needed to execute automated scripts.

## Requirements

* Python 3.11 or later
* Google Chrome installation

## Overview

ChromeDriver wraps functionality commonly used when creating automated scripts. The simple interface allows easy usage of the package and minimizes redundant code needed by web automation projects.

## Installation

To install the package, run

```
pip install git+https://github.com/elias-a/ChromeDriver.git
```

## Usage

The simplest usage of the package involves instantiating the `ChromeDriver` class with no arguments:

```
chromedriver = ChromeDriver()
chromedriver.driver.get("https://github.com")
```

The `ChromeDriver` class contains an instance variable `driver` that is an instance of `selenium.webdriver.chrome.webdriver.WebDriver` and can be used identically to the standard selenium chromedriver.

Optionally, you can specify the Chrome version and the user data directory the browser instance should use:

```
profile = "/path/to/chrome/user_data_dir"
chromeVersion = 110
chromedriver = ChromeDriver(profile=profile, chromeVersion=chromeVersion)
```

If no Chrome version is specified, the package searches for the installed version of Chrome on your machine. This functionality currently only works on Linux.
