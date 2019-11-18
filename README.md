# YTViewer

**YTViewer** is simple YouTube views bot. Reuploaded by Ethan Nadzieja. This repository will not be updated. See [ytviewer's Gitlab](https://gitlab.com/DeBos/ytviewer) for updates.

## Content

- [Content](#content)
- [Features](#features)
- [Installation](#installation)
  - [Windows](#windows)
  - [Unix](#unix)
    - [Debian/Ubuntu](#apt)
    - [Arch Linux/Manjaro](#pacman)
    - [CentOS](#yum)
    - [MacOS](#homebrew)
- [Usage](#usage)
- [Documentation](#documentation)
  - [Required arguments](#required-arguments)
  - [Optional arguments](#optional-arguments)
- [Disclaimer](#disclaimer)
- [Authors](#authors)
- [Contact](#contact)
- [License](#license)

## Features

* Multi-threaded.
* Support for multiple URLs.
* Support for ChromeDriver and GeckoDriver.
* Headless mode.
* Slow start mode for older machines.
* Configurable view duration.
* IP and User agent rotation.
* Referer spoofing.
* Debug mode.

## Installation

### Windows

* Install [Git](https://git-scm.com/download/win).
* Install [Python](https://www.python.org/downloads/).
* Install [Google Chrome](https://www.google.com/chrome/).
<br>Or
<br>Install [Firefox](https://www.mozilla.org/firefox/new/).
* Run following command in the command prompt:
```
git clone "https://github.com/DeBos99/ytviewer.git"
```

### Unix

#### <a name="APT">Debian/Ubuntu based

* Run following commands in the terminal:
```
sudo apt install git python -y
git clone "https://github.com/DeBos99/ytviewer.git"
```

#### <a name="Pacman">Arch Linux/Manjaro

* Run following commands in the terminal:
```
sudo pacman -S git python --noconfirm
git clone "https://github.com/DeBos99/ytviewer.git"
```

#### <a name="YUM">CentOS

* Run following commands in the terminal:
```
sudo yum install git python -y
git clone "https://github.com/DeBos99/ytviewer.git"
```

#### <a name="Homebrew">MacOS

* Run following commands in the terminal:
```
brew install git python
git clone "https://github.com/DeBos99/ytviewer.git"
```

## Usage

`python main.py ARGUMENTS`

## Documentation

### Required arguments

| Argument       | Description                  |
| :------------- | :--------------------------- |
| -u, --url URL  | Sets url of video.           |
| -u, --url PATH | Sets path to file with urls. |

### Optional arguments

| Argument                      | Description                              | Default value                  |
| :---------------------------- | :--------------------------------------- | :----------------------------- |
| -h, --help                    | Shows help message and exits.            |                                |
| -t, --threads N               | Sets number of threads.                  | 15                             |
| -D, --driver {chrome,firefox} | Sets webdriver.                          | chrome                         |
| -H, --headless                | Enables headless mode.                   | False                          |
| -s, --slow-start              | Enables slow start mode.                 | False                          |
| -du, --duration N             | Sets duration of view in seconds.        | Video duration.                |
| -p, --proxies PATH            | Sets path to file with proxies.          | Proxies list from internet.    |
| -U, --user-agent AGENT        | Sets user agent.                         | Randomly generated user agent. |
| -U, --user-agent PATH         | Sets path to file with user agents.      |                                |
| -R, --referer REFERER         | Sets referer.                            | https://google.com             |
| -R, --referer PATH            | Sets path to file with referer.          |                                |
| -d, --debug                   | Enables debug mode.                      | False                          |
| -r, --refresh N               | Sets refresh rate for logger in seconds. | 1.0                            |

## Disclaimer

**YTViewer** was created for educational purposes and I'm not taking responsibility for any of your actions.

## Authors

* **Michał Wróblewski** - Main Developer - DeBos99


[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=NH8JV53DSVDMY)

See also the list of [contributors](https://github.com/etz/ytviewer/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
