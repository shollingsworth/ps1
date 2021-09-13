[![github-issues](https://img.shields.io/github/issues/shollingsworth/ps1?style=plastic "github-issues")](https://github.com/shollingsworth/ps1/issues) [![github-languages-code-size](https://img.shields.io/github/languages/code-size/shollingsworth/ps1?style=plastic "github-languages-code-size")](https://github.com/shollingsworth/ps1) [![github-stars](https://img.shields.io/github/stars/shollingsworth/ps1?style=plastic "github-stars")](https://github.com/shollingsworth/ps1/stargazers) [![github-forks](https://img.shields.io/github/forks/shollingsworth/ps1?style=plastic "github-forks")](https://github.com/shollingsworth/ps1/network/members) 

[![pypi-v](https://img.shields.io/pypi/v/ps1?style=plastic "pypi-v")](https://pypi.org/project/ps1) [![pypi-status](https://img.shields.io/pypi/status/ps1?style=plastic "pypi-status")](https://pypi.org/project/ps1) [![pypi-l](https://img.shields.io/pypi/l/ps1?style=plastic "pypi-l")](https://pypi.org/project/ps1) [![pypi-dm](https://img.shields.io/pypi/dm/ps1?style=plastic "pypi-dm")](https://pypi.org/project/ps1) [![pypi-pyversions](https://img.shields.io/pypi/pyversions/ps1?style=plastic "pypi-pyversions")](https://pypi.org/project/ps1) [![pypi-implementation](https://img.shields.io/pypi/implementation/ps1?style=plastic "pypi-implementation")](https://pypi.org/project/ps1) 

# TOC
* [PS1](#ps1-)
   * [Installation](#installation-)
   * [License](#license-)
   * [Quickstart](#quickstart-)
   * [PS1 Command](#ps1-command-)
   * [Examples](#examples-)
   * [Other Docs](#other-docs-)


# PS1 [&#8593;](#toc)
This program is meant to take the pain out of generating nice bash PS1 prompts.

Pull requests welcome! And if you build an awesome theme, drop something in the [examples](./src/ps1api/examples) folder!
## Installation [&#8593;](#toc)
To install this package from [pypy](https://pypi.org/project/ps1/) run the following command.


```

pip3 install ps1

```

## License [&#8593;](#toc)
See: [LICENSE](./LICENSE)
## Quickstart [&#8593;](#toc)
Here's an example to get you up and running!


```

pip3 install ps1

export PS1="$(ps1 template -t parrot)"

```

## PS1 Command [&#8593;](#toc)
### Custom
```
usage: ps1 custom [-h] [--add_bash_ver color title] [--add_bash_ver_release color title] [--add_cmd_num color title]
                        [--add_custom value color title] [--add_date_time_24hr color title] [--add_date_week_month_day color title]
                        [--add_exit_code ok_txt err_txt ok_color err_color title] [--add_git_branch color title]
                        [--add_hist_num color title] [--add_host color title] [--add_host_long color title] [--add_jobs color title]
                        [--add_newline] [--add_shell_name color title] [--add_term_base color title]
                        [--add_time_12hr_am_pm color title] [--add_time_12hr_with_second color title] [--add_time_24 color title]
                        [--add_user color title] [--add_user_host user_color at_sym_color host_color]
                        [--add_working_dir_basename color title] [--add_working_directory color title] [--set_ends start end]
                        [--set_fancy_lines] [--set_no_color value] [--set_prompt_color color] [--set_section_color color]
                        [--set_section_delim delim]

optional arguments:
  -h, --help            show this help message and exit
  --add_bash_ver color title
                        Add The version of Bash (e.g., 2.00).
  --add_bash_ver_release color title
                        Add The release of Bash, version + patchlevel (e.g., 2.00.0).
  --add_cmd_num color title
                        Add Number of commands this terminal has run.
  --add_custom value color title
                        Add custom section value/color.
  --add_date_time_24hr color title
                        Add the date/time, in 24-hour HH:MM:SS format.
                        ::
                            Mon Sep 13 10:28:40
  --add_date_week_month_day color title
                        Add Date week month day.
                        ::
                            Mon Sep 13
  --add_exit_code ok_txt err_txt ok_color err_color title
                        Add Exit code indicator to prompt.
  --add_git_branch color title
                        Add git branch to prompt.
  --add_hist_num color title
                        Add History count.
  --add_host color title
                        Add PS1 host expansion value.
  --add_host_long color title
                        Add PS1 host expansion value.
  --add_jobs color title
                        Add The number of jobs currently managed by the shell.
  --add_newline         Insert newline.
  --add_shell_name color title
                        Add The name of the shell, the basename of $0 (the portion following the final slash).
  --add_term_base color title
                        Add The basename of the shell's terminal device name.
  --add_time_12hr_am_pm color title
                        Add The time, in 12-hour am/pm format.
                        ::
                            10:28 AM
  --add_time_12hr_with_second color title
                        Add The time, in 12-hour HH:MM:SS format.
                        ::
                            10:28:40
  --add_time_24 color title
                        Add The time, in 24-hour HH:MM:SS format.
                        ::
                            10:28:40
  --add_user color title
                        Add PS1 user expansion value.
  --add_user_host user_color at_sym_color host_color
                        Add User/Host to prompt.
                        ::
                            [user@hostname]-[section2]
                                  ^ add this
  --add_working_dir_basename color title
                        Add The basename of $PWD.
  --add_working_directory color title
                        Add Working directory to prompt.
                        ::
                            [user@hostame]─[~/path/i/am/in]
                                             ^ add this
  --set_ends start end  Set Section start / end values.
                        ::
                            {}
                            {section1}-{section2}
                        
                            []
                            [section1]-[section2]
                        
                            ❰❱
                            ❰section1❱-❰section2❱
  --set_fancy_lines     Set fancy line breaks like the following
                        ::
                            ┌───
                            ├───
                            └──╼
  --set_no_color value  Set terminal to no color.
  --set_prompt_color color
                        Set prompt color.
                        ::
                            i.e. $ or # depending on user
  --set_section_color color
                        Set default section color.
  --set_section_delim delim
                        Set section separator.
                        ::
                            i.e. [section1]-[section2]
                                           ^ separator

```


### Examples
```
usage: ps1 examples [-h]

optional arguments:
  -h, --help  show this help message and exit

```


### Listcolors
```
usage: ps1 listcolors [-h] [--filter FILTER]

optional arguments:
  -h, --help            show this help message and exit
  --filter FILTER, -f FILTER
                        Filter color values

```


### Template
```
usage: ps1 template [-h] [-t TEMPLATE_NAME] [-l]

optional arguments:
  -h, --help            show this help message and exit
  -t TEMPLATE_NAME, --template_name TEMPLATE_NAME
                        Template Name
  -l, --list            List Templates

```


## Examples [&#8593;](#toc)
### [entropy.sh](https://github.com/shollingsworth/ps1/blob/main/src/ps1api/examples/dark/entropy.sh)
![entropy.sh](https://raw.githubusercontent.com/shollingsworth/ps1/main/media/dark/entropy.sh.png)


### [filecount.sh](https://github.com/shollingsworth/ps1/blob/main/src/ps1api/examples/dark/filecount.sh)
![filecount.sh](https://raw.githubusercontent.com/shollingsworth/ps1/main/media/dark/filecount.sh.png)


### [greenguy.sh](https://github.com/shollingsworth/ps1/blob/main/src/ps1api/examples/dark/greenguy.sh)
![greenguy.sh](https://raw.githubusercontent.com/shollingsworth/ps1/main/media/dark/greenguy.sh.png)


### [ips.sh](https://github.com/shollingsworth/ps1/blob/main/src/ps1api/examples/dark/ips.sh)
![ips.sh](https://raw.githubusercontent.com/shollingsworth/ps1/main/media/dark/ips.sh.png)


### [parrot.sh](https://github.com/shollingsworth/ps1/blob/main/src/ps1api/examples/dark/parrot.sh)
![parrot.sh](https://raw.githubusercontent.com/shollingsworth/ps1/main/media/dark/parrot.sh.png)


### [plainjane.sh](https://github.com/shollingsworth/ps1/blob/main/src/ps1api/examples/dark/plainjane.sh)
![plainjane.sh](https://raw.githubusercontent.com/shollingsworth/ps1/main/media/dark/plainjane.sh.png)


### [purplegoblin.sh](https://github.com/shollingsworth/ps1/blob/main/src/ps1api/examples/dark/purplegoblin.sh)
![purplegoblin.sh](https://raw.githubusercontent.com/shollingsworth/ps1/main/media/dark/purplegoblin.sh.png)


### [skulls.sh](https://github.com/shollingsworth/ps1/blob/main/src/ps1api/examples/dark/skulls.sh)
![skulls.sh](https://raw.githubusercontent.com/shollingsworth/ps1/main/media/dark/skulls.sh.png)


### [stev0_work.sh](https://github.com/shollingsworth/ps1/blob/main/src/ps1api/examples/dark/stev0_work.sh)
![stev0_work.sh](https://raw.githubusercontent.com/shollingsworth/ps1/main/media/dark/stev0_work.sh.png)


### [too_many_options.sh](https://github.com/shollingsworth/ps1/blob/main/src/ps1api/examples/dark/too_many_options.sh)
![too_many_options.sh](https://raw.githubusercontent.com/shollingsworth/ps1/main/media/dark/too_many_options.sh.png)


### [fire_ice.sh](https://github.com/shollingsworth/ps1/blob/main/src/ps1api/examples/light/fire_ice.sh)
![fire_ice.sh](https://raw.githubusercontent.com/shollingsworth/ps1/main/media/light/fire_ice.sh.png)


### [magenta.sh](https://github.com/shollingsworth/ps1/blob/main/src/ps1api/examples/light/magenta.sh)
![magenta.sh](https://raw.githubusercontent.com/shollingsworth/ps1/main/media/light/magenta.sh.png)


### [powderpuff.sh](https://github.com/shollingsworth/ps1/blob/main/src/ps1api/examples/light/powderpuff.sh)
![powderpuff.sh](https://raw.githubusercontent.com/shollingsworth/ps1/main/media/light/powderpuff.sh.png)


## Other Docs [&#8593;](#toc)
* [Api Docs](https://shollingsworth.github.io/ps1/)
* [Changelog](./CHANGELOG.md)
