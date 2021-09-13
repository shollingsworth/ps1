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
```
export PS1='\[\e[38;5;196m\]\000\342\224\214\000\342\224\200\000\342\224\200\[\e[0m\]\[\e[38;5;196m\]\000\342\235\260\[\e[0m\]$(b_err_code=$?; [[ $b_err_code != 0 ]] && echo "\[\e[38;5;196m\]\000\342\234\230\[\e[0m\]/${b_err_code}" || echo "\[\e[38;5;10m\]\000\342\234\224\[\e[0m\]")\[\e[38;5;196m\]\000\342\235\261\[\e[0m\]\[\e[38;5;196m\]\000\342\224\201\[\e[0m\]\[\e[38;5;196m\]\000\342\235\260\[\e[0m\]entropy:$(_shentropy)\[\e[38;5;196m\]\000\342\235\261\[\e[0m\]\[\e[38;5;196m\]\000\342\224\201\[\e[0m\]\[\e[38;5;196m\]\000\342\235\260\[\e[0m\]\[\e[38;5;11m\]$(br=$(git branch 2>/dev/null| grep '"'"'^\*'"'"' | awk '"'"'{print $NF}'"'"'); [[ "${br}" ]] && echo "${br}" || echo "-")\[\e[0m\]\[\e[38;5;196m\]\000\342\235\261\[\e[0m\]\n\[\e[38;5;196m\]\000\342\224\234\000\342\224\200\000\342\224\200\[\e[0m\]\[\e[38;5;196m\]\000\342\235\260\[\e[0m\]\[\e[38;5;10m\]\w\[\e[0m\]\[\e[38;5;196m\]\000\342\235\261\[\e[0m\]\n\[\e[38;5;196m\]\000\342\224\224\000\342\224\200\000\342\225\274\[\e[0m\] \[\e[38;5;11m\]\$ \[\e[0m\]'
```
![entropy.sh](https://raw.githubusercontent.com/shollingsworth/ps1/main/media/dark/entropy.sh.png)


### [face.sh](https://github.com/shollingsworth/ps1/blob/main/src/ps1api/examples/dark/face.sh)
```
export PS1='\[\e[38;5;15m\]\[\e[1m\]\000\342\224\214\000\342\224\200\000\342\224\200\[\e[0m\]\[\e[38;5;15m\]\[\e[1m\]\000\342\235\260\[\e[0m\]$(b_err_code=$?; [[ $b_err_code != 0 ]] && echo "\[\e[38;5;196m\]\000\342\234\230\[\e[0m\]/${b_err_code}" || echo "\[\e[38;5;10m\]\000\342\234\224\[\e[0m\]")\[\e[38;5;15m\]\[\e[1m\]\000\342\235\261\[\e[0m\]\[\e[38;5;15m\]\[\e[1m\]\360\237\230\235\[\e[0m\]\[\e[38;5;15m\]\[\e[1m\]\000\342\235\260\[\e[0m\]\[\e[38;5;248m\]\u\[\e[0m\]\[\e[38;5;15m\]@\[\e[0m\]\[\e[38;5;248m\]\h\[\e[0m\]\[\e[38;5;15m\]\[\e[1m\]\000\342\235\261\[\e[0m\]\[\e[38;5;15m\]\[\e[1m\]\360\237\230\235\[\e[0m\]\[\e[38;5;15m\]\[\e[1m\]\000\342\235\260\[\e[0m\]\[\e[38;5;238m\]\[\e[1m\]\w\[\e[0m\]\[\e[38;5;15m\]\[\e[1m\]\000\342\235\261\[\e[0m\]\n\[\e[38;5;15m\]\[\e[1m\]\000\342\224\234\000\342\224\200\000\342\224\200\[\e[0m\]\[\e[38;5;15m\]\[\e[1m\]\000\342\235\260\[\e[0m\]\[\e[38;5;196m\]$(br=$(git branch 2>/dev/null| grep '"'"'^\*'"'"' | awk '"'"'{print $NF}'"'"'); [[ "${br}" ]] && echo "${br}" || echo "-")\[\e[0m\]\[\e[38;5;15m\]\[\e[1m\]\000\342\235\261\[\e[0m\]\n\[\e[38;5;15m\]\[\e[1m\]\000\342\224\224\000\342\224\200\000\342\225\274\[\e[0m\] \[\e[38;5;10m\]\$ \[\e[0m\]'
```
![face.sh](https://raw.githubusercontent.com/shollingsworth/ps1/main/media/dark/face.sh.png)


### [filecount.sh](https://github.com/shollingsworth/ps1/blob/main/src/ps1api/examples/dark/filecount.sh)
```
export PS1='\[\e[38;5;10m\]\000\342\224\214\000\342\224\200\000\342\224\200\[\e[0m\]\[\e[38;5;10m\]\000\342\235\260\[\e[0m\]$(b_err_code=$?; [[ $b_err_code != 0 ]] && echo "\[\e[38;5;196m\]\000\342\234\230\[\e[0m\]/${b_err_code}" || echo "\[\e[38;5;10m\]\000\342\234\224\[\e[0m\]")\[\e[38;5;10m\]\000\342\235\261\[\e[0m\]\[\e[38;5;10m\]\000\342\224\201\[\e[0m\]\[\e[38;5;10m\]\000\342\235\260\[\e[0m\]\[\e[38;5;11m\]$(br=$(git branch 2>/dev/null| grep '"'"'^\*'"'"' | awk '"'"'{print $NF}'"'"'); [[ "${br}" ]] && echo "${br}" || echo "-")\[\e[0m\]\[\e[38;5;10m\]\000\342\235\261\[\e[0m\]\n\[\e[38;5;10m\]\000\342\224\234\000\342\224\200\000\342\224\200\[\e[0m\]\[\e[38;5;10m\]\000\342\235\260\[\e[0m\]\[\e[38;5;196m\]fcnt:$(_fcount)\[\e[0m\]\[\e[38;5;10m\]\000\342\235\261\[\e[0m\]\[\e[38;5;10m\]\000\342\224\201\[\e[0m\]\[\e[38;5;10m\]\000\342\235\260\[\e[0m\]\[\e[38;5;5m\]fsize:$(_dirfilesize)\[\e[0m\]\[\e[38;5;10m\]\000\342\235\261\[\e[0m\]\n\[\e[38;5;10m\]\000\342\224\224\000\342\224\200\000\342\225\274\[\e[0m\]\[\e[38;5;10m\]\000\342\235\260\[\e[0m\]\[\e[38;5;196m\]\w\[\e[0m\]\[\e[38;5;10m\]\000\342\235\261\[\e[0m\]\[\e[38;5;10m\]\000\342\224\201\[\e[0m\]\[\e[38;5;10m\]\000\342\235\260\[\e[0m\]\[\e[38;5;247m\]\u\[\e[0m\]\[\e[38;5;11m\]@\[\e[0m\]\[\e[38;5;12m\]\h\[\e[0m\]\[\e[38;5;10m\]\000\342\235\261\[\e[0m\] \[\e[38;5;10m\]\$ \[\e[0m\]'
```
![filecount.sh](https://raw.githubusercontent.com/shollingsworth/ps1/main/media/dark/filecount.sh.png)


### [greenguy.sh](https://github.com/shollingsworth/ps1/blob/main/src/ps1api/examples/dark/greenguy.sh)
```
export PS1='\[\e[38;5;10m\]\000\342\224\214\000\342\224\200\000\342\224\200\[\e[0m\]\[\e[38;5;10m\]\000\342\235\260\[\e[0m\]$(b_err_code=$?; [[ $b_err_code != 0 ]] && echo "\[\e[38;5;196m\]\000\342\234\230\[\e[0m\]/${b_err_code}" || echo "\[\e[38;5;10m\]\000\342\234\224\[\e[0m\]")\[\e[38;5;10m\]\000\342\235\261\[\e[0m\]\[\e[38;5;10m\]\000\342\224\201\[\e[0m\]\[\e[38;5;10m\]\000\342\235\260\[\e[0m\]\[\e[38;5;247m\]\u\[\e[0m\]\[\e[38;5;11m\]@\[\e[0m\]\[\e[38;5;12m\]\h\[\e[0m\]\[\e[38;5;10m\]\000\342\235\261\[\e[0m\]\[\e[38;5;10m\]\000\342\224\201\[\e[0m\]\[\e[38;5;10m\]\000\342\235\260\[\e[0m\]\[\e[38;5;196m\]\w\[\e[0m\]\[\e[38;5;10m\]\000\342\235\261\[\e[0m\]\n\[\e[38;5;10m\]\000\342\224\234\000\342\224\200\000\342\224\200\[\e[0m\]\[\e[38;5;10m\]\000\342\235\260\[\e[0m\]\[\e[38;5;11m\]$(br=$(git branch 2>/dev/null| grep '"'"'^\*'"'"' | awk '"'"'{print $NF}'"'"'); [[ "${br}" ]] && echo "${br}" || echo "-")\[\e[0m\]\[\e[38;5;10m\]\000\342\235\261\[\e[0m\]\n\[\e[38;5;10m\]\000\342\224\224\000\342\224\200\000\342\225\274\[\e[0m\] \[\e[38;5;10m\]\$ \[\e[0m\]'
```
![greenguy.sh](https://raw.githubusercontent.com/shollingsworth/ps1/main/media/dark/greenguy.sh.png)


### [ips.sh](https://github.com/shollingsworth/ps1/blob/main/src/ps1api/examples/dark/ips.sh)
```
export PS1='\[\e[38;5;196m\]\[\e[1m\]\000\342\224\214\000\342\224\200\000\342\224\200\[\e[0m\]\[\e[38;5;196m\]\[\e[1m\]\000\342\235\260\[\e[0m\]$(b_err_code=$?; [[ $b_err_code != 0 ]] && echo "\[\e[38;5;196m\]\000\342\234\230\[\e[0m\]/${b_err_code}" || echo "\[\e[38;5;2m\]\000\342\234\224\[\e[0m\]")\[\e[38;5;196m\]\[\e[1m\]\000\342\235\261\[\e[0m\]\[\e[38;5;196m\]\[\e[1m\]\000\342\224\201\[\e[0m\]\[\e[38;5;196m\]\[\e[1m\]\000\342\235\260\[\e[0m\]entropy:$(_shentropy)\[\e[38;5;196m\]\[\e[1m\]\000\342\235\261\[\e[0m\]\n\[\e[38;5;196m\]\[\e[1m\]\000\342\224\234\000\342\224\200\000\342\224\200\[\e[0m\]\[\e[38;5;196m\]\[\e[1m\]\000\342\235\260\[\e[0m\]\[\e[38;5;11m\]$(br=$(git branch 2>/dev/null| grep '"'"'^\*'"'"' | awk '"'"'{print $NF}'"'"'); [[ "${br}" ]] && echo "${br}" || echo "-")\[\e[0m\]\[\e[38;5;196m\]\[\e[1m\]\000\342\235\261\[\e[0m\]\[\e[38;5;196m\]\[\e[1m\]\000\342\224\201\[\e[0m\]\[\e[38;5;196m\]\[\e[1m\]\000\342\235\260\[\e[0m\]ips:$(_ips)\[\e[38;5;196m\]\[\e[1m\]\000\342\235\261\[\e[0m\]\n\[\e[38;5;196m\]\[\e[1m\]\000\342\224\234\000\342\224\200\000\342\224\200\[\e[0m\]\[\e[38;5;196m\]\[\e[1m\]\000\342\235\260\[\e[0m\]\[\e[38;5;33m\]\w\[\e[0m\]\[\e[38;5;196m\]\[\e[1m\]\000\342\235\261\[\e[0m\]\n\[\e[38;5;196m\]\[\e[1m\]\000\342\224\224\000\342\224\200\000\342\225\274\[\e[0m\] \[\e[38;5;15m\]\$ \[\e[0m\]'
```
![ips.sh](https://raw.githubusercontent.com/shollingsworth/ps1/main/media/dark/ips.sh.png)


### [parrot.sh](https://github.com/shollingsworth/ps1/blob/main/src/ps1api/examples/dark/parrot.sh)
```
export PS1='\[\e[38;5;196m\]\000\342\224\214\000\342\224\200\000\342\224\200\[\e[0m\]\[\e[38;5;196m\]\000\342\235\260\[\e[0m\]$(b_err_code=$?; [[ $b_err_code != 0 ]] && echo "\[\e[38;5;196m\]\000\342\234\230\[\e[0m\]/${b_err_code}" || echo "\[\e[38;5;10m\]\000\342\234\224\[\e[0m\]")\[\e[38;5;196m\]\000\342\235\261\[\e[0m\]\[\e[38;5;196m\]\000\342\224\201\[\e[0m\]\[\e[38;5;196m\]\000\342\235\260\[\e[0m\]\[\e[38;5;247m\]\u\[\e[0m\]\[\e[38;5;11m\]@\[\e[0m\]\[\e[38;5;12m\]\h\[\e[0m\]\[\e[38;5;196m\]\000\342\235\261\[\e[0m\]\[\e[38;5;196m\]\000\342\224\201\[\e[0m\]\[\e[38;5;196m\]\000\342\235\260\[\e[0m\]\[\e[38;5;10m\]\w\[\e[0m\]\[\e[38;5;196m\]\000\342\235\261\[\e[0m\]\n\[\e[38;5;196m\]\000\342\224\234\000\342\224\200\000\342\224\200\[\e[0m\]\[\e[38;5;196m\]\000\342\235\260\[\e[0m\]\[\e[38;5;11m\]$(br=$(git branch 2>/dev/null| grep '"'"'^\*'"'"' | awk '"'"'{print $NF}'"'"'); [[ "${br}" ]] && echo "${br}" || echo "-")\[\e[0m\]\[\e[38;5;196m\]\000\342\235\261\[\e[0m\]\n\[\e[38;5;196m\]\000\342\224\224\000\342\224\200\000\342\225\274\[\e[0m\] \[\e[38;5;11m\]\$ \[\e[0m\]'
```
![parrot.sh](https://raw.githubusercontent.com/shollingsworth/ps1/main/media/dark/parrot.sh.png)


### [plainjane.sh](https://github.com/shollingsworth/ps1/blob/main/src/ps1api/examples/dark/plainjane.sh)
```
export PS1='$(b_err_code=$?; [[ $b_err_code != 0 ]] && echo "✘/${b_err_code}" || echo "✔") \w \$'
```
![plainjane.sh](https://raw.githubusercontent.com/shollingsworth/ps1/main/media/dark/plainjane.sh.png)


### [purplegoblin.sh](https://github.com/shollingsworth/ps1/blob/main/src/ps1api/examples/dark/purplegoblin.sh)
```
export PS1='\[\e[38;5;5m\]\000\342\224\214\000\342\224\200\000\342\224\200\[\e[0m\]\[\e[38;5;5m\]\000\342\235\260\[\e[0m\]$(b_err_code=$?; [[ $b_err_code != 0 ]] && echo "\[\e[38;5;196m\]\000\342\234\230\[\e[0m\]/${b_err_code}" || echo "\[\e[38;5;10m\]\000\342\234\224\[\e[0m\]")\[\e[38;5;5m\]\000\342\235\261\[\e[0m\]\[\e[38;5;5m\]\000\342\224\201\[\e[0m\]\[\e[38;5;5m\]\000\342\235\260\[\e[0m\]\[\e[38;5;247m\]\u\[\e[0m\]\[\e[38;5;11m\]@\[\e[0m\]\[\e[38;5;12m\]\h\[\e[0m\]\[\e[38;5;5m\]\000\342\235\261\[\e[0m\]\[\e[38;5;5m\]\000\342\224\201\[\e[0m\]\[\e[38;5;5m\]\000\342\235\260\[\e[0m\]\[\e[38;5;10m\]\w\[\e[0m\]\[\e[38;5;5m\]\000\342\235\261\[\e[0m\]\n\[\e[38;5;5m\]\000\342\224\234\000\342\224\200\000\342\224\200\[\e[0m\]\[\e[38;5;5m\]\000\342\235\260\[\e[0m\]\[\e[38;5;11m\]$(br=$(git branch 2>/dev/null| grep '"'"'^\*'"'"' | awk '"'"'{print $NF}'"'"'); [[ "${br}" ]] && echo "${br}" || echo "-")\[\e[0m\]\[\e[38;5;5m\]\000\342\235\261\[\e[0m\]\n\[\e[38;5;5m\]\000\342\224\224\000\342\224\200\000\342\225\274\[\e[0m\] \[\e[38;5;10m\]\$ \[\e[0m\]'
```
![purplegoblin.sh](https://raw.githubusercontent.com/shollingsworth/ps1/main/media/dark/purplegoblin.sh.png)


### [skulls.sh](https://github.com/shollingsworth/ps1/blob/main/src/ps1api/examples/dark/skulls.sh)
```
export PS1='\[\e[38;5;15m\]\[\e[1m\]\000\342\224\214\000\342\224\200\000\342\224\200\[\e[0m\]\[\e[38;5;15m\]\[\e[1m\]\000\342\235\260\[\e[0m\]$(b_err_code=$?; [[ $b_err_code != 0 ]] && echo "\[\e[38;5;196m\]\000\342\234\230\[\e[0m\]/${b_err_code}" || echo "\[\e[38;5;10m\]\000\342\234\224\[\e[0m\]")\[\e[38;5;15m\]\[\e[1m\]\000\342\235\261\[\e[0m\]\[\e[38;5;15m\]\[\e[1m\]\360\237\222\200\[\e[0m\]\[\e[38;5;15m\]\[\e[1m\]\000\342\235\260\[\e[0m\]\[\e[38;5;248m\]\u\[\e[0m\]\[\e[38;5;15m\]@\[\e[0m\]\[\e[38;5;248m\]\h\[\e[0m\]\[\e[38;5;15m\]\[\e[1m\]\000\342\235\261\[\e[0m\]\[\e[38;5;15m\]\[\e[1m\]\360\237\222\200\[\e[0m\]\[\e[38;5;15m\]\[\e[1m\]\000\342\235\260\[\e[0m\]\[\e[38;5;238m\]\[\e[1m\]\w\[\e[0m\]\[\e[38;5;15m\]\[\e[1m\]\000\342\235\261\[\e[0m\]\n\[\e[38;5;15m\]\[\e[1m\]\000\342\224\234\000\342\224\200\000\342\224\200\[\e[0m\]\[\e[38;5;15m\]\[\e[1m\]\000\342\235\260\[\e[0m\]\[\e[38;5;196m\]$(br=$(git branch 2>/dev/null| grep '"'"'^\*'"'"' | awk '"'"'{print $NF}'"'"'); [[ "${br}" ]] && echo "${br}" || echo "-")\[\e[0m\]\[\e[38;5;15m\]\[\e[1m\]\000\342\235\261\[\e[0m\]\[\e[38;5;15m\]\[\e[1m\]\360\237\222\200\[\e[0m\]\[\e[38;5;15m\]\[\e[1m\]\000\342\235\260\[\e[0m\]\[\e[38;5;0m\]\[\e[48;5;238m\]rando_str:$(_randstr)\[\e[0m\]\[\e[38;5;15m\]\[\e[1m\]\000\342\235\261\[\e[0m\]\n\[\e[38;5;15m\]\[\e[1m\]\000\342\224\224\000\342\224\200\000\342\225\274\[\e[0m\] \[\e[38;5;10m\]\$ \[\e[0m\]'
```
![skulls.sh](https://raw.githubusercontent.com/shollingsworth/ps1/main/media/dark/skulls.sh.png)


### [stev0_work.sh](https://github.com/shollingsworth/ps1/blob/main/src/ps1api/examples/dark/stev0_work.sh)
```
export PS1='\[\e[38;5;196m\]\[\e[1m\]\133\[\e[0m\]$(b_err_code=$?; [[ $b_err_code != 0 ]] && echo "\[\e[38;5;196m\]\000\342\234\230\[\e[0m\]/${b_err_code}" || echo "\[\e[38;5;2m\]\000\342\234\224\[\e[0m\]")\[\e[38;5;196m\]\[\e[1m\]\135\[\e[0m\]\[\e[38;5;196m\]\[\e[1m\]\[\e[0m\]\[\e[38;5;196m\]\[\e[1m\]\133\[\e[0m\]entropy:$(_shentropy)\[\e[38;5;196m\]\[\e[1m\]\135\[\e[0m\]\[\e[38;5;196m\]\[\e[1m\]\[\e[0m\]\[\e[38;5;196m\]\[\e[1m\]\133\[\e[0m\]\[\e[38;5;2m\]\d \t\[\e[0m\]\[\e[38;5;196m\]\[\e[1m\]\135\[\e[0m\]\[\e[38;5;196m\]\[\e[1m\]\[\e[0m\]\[\e[38;5;196m\]\[\e[1m\]\133\[\e[0m\]jobs:\[\e[38;5;196m\]\j\[\e[0m\]\[\e[38;5;196m\]\[\e[1m\]\135\[\e[0m\]\[\e[38;5;196m\]\[\e[1m\]\[\e[0m\]\[\e[38;5;196m\]\[\e[1m\]\133\[\e[0m\]cmd#:\[\e[38;5;196m\]\#\[\e[0m\]\[\e[38;5;196m\]\[\e[1m\]\135\[\e[0m\]\n\[\e[38;5;196m\]\[\e[1m\]\133\[\e[0m\]\[\e[38;5;33m\]\w\[\e[0m\]\[\e[38;5;196m\]\[\e[1m\]\135\[\e[0m\]\[\e[38;5;196m\]\[\e[1m\]\[\e[0m\]\[\e[38;5;196m\]\[\e[1m\]\133\[\e[0m\]\[\e[38;5;11m\]$(br=$(git branch 2>/dev/null| grep '"'"'^\*'"'"' | awk '"'"'{print $NF}'"'"'); [[ "${br}" ]] && echo "${br}" || echo "-")\[\e[0m\]\[\e[38;5;196m\]\[\e[1m\]\135\[\e[0m\]\n \[\e[38;5;15m\]\$ \[\e[0m\]'
```
![stev0_work.sh](https://raw.githubusercontent.com/shollingsworth/ps1/main/media/dark/stev0_work.sh.png)


### [too_many_options.sh](https://github.com/shollingsworth/ps1/blob/main/src/ps1api/examples/dark/too_many_options.sh)
```
export PS1='\[\e[38;5;196m\]\000\342\224\214\000\342\224\200\000\342\224\200\[\e[0m\]\[\e[38;5;196m\]\000\342\235\260\[\e[0m\]$(b_err_code=$?; [[ $b_err_code != 0 ]] && echo "\[\e[38;5;196m\]\000\342\234\230\[\e[0m\]/${b_err_code}" || echo "\[\e[38;5;10m\]\000\342\234\224\[\e[0m\]")\[\e[38;5;196m\]\000\342\235\261\[\e[0m\]\n\[\e[38;5;196m\]\000\342\224\234\000\342\224\200\000\342\224\200\[\e[0m\]\[\e[38;5;196m\]\000\342\235\260\[\e[0m\]entropy:$(_shentropy)\[\e[38;5;196m\]\000\342\235\261\[\e[0m\]\n\[\e[38;5;196m\]\000\342\224\234\000\342\224\200\000\342\224\200\[\e[0m\]\[\e[38;5;196m\]\000\342\235\260\[\e[0m\]git:\[\e[38;5;10m\]$(br=$(git branch 2>/dev/null| grep '"'"'^\*'"'"' | awk '"'"'{print $NF}'"'"'); [[ "${br}" ]] && echo "${br}" || echo "-")\[\e[0m\]\[\e[38;5;196m\]\000\342\235\261\[\e[0m\]\n\[\e[38;5;196m\]\000\342\224\234\000\342\224\200\000\342\224\200\[\e[0m\]\[\e[38;5;196m\]\000\342\235\260\[\e[0m\]user:\[\e[38;5;10m\]\u\[\e[0m\]\[\e[38;5;196m\]\000\342\235\261\[\e[0m\]\[\e[38;5;196m\]\000\342\224\201\[\e[0m\]\[\e[38;5;196m\]\000\342\235\260\[\e[0m\]\[\e[38;5;247m\]\u\[\e[0m\]\[\e[38;5;11m\]@\[\e[0m\]\[\e[38;5;12m\]\h\[\e[0m\]\[\e[38;5;196m\]\000\342\235\261\[\e[0m\]\n\[\e[38;5;196m\]\000\342\224\234\000\342\224\200\000\342\224\200\[\e[0m\]\[\e[38;5;196m\]\000\342\235\260\[\e[0m\]working_dir_basename:\[\e[38;5;10m\]\W\[\e[0m\]\[\e[38;5;196m\]\000\342\235\261\[\e[0m\]\[\e[38;5;196m\]\000\342\224\201\[\e[0m\]\[\e[38;5;196m\]\000\342\235\260\[\e[0m\]working_dir:\[\e[38;5;10m\]\w\[\e[0m\]\[\e[38;5;196m\]\000\342\235\261\[\e[0m\]\n\[\e[38;5;196m\]\000\342\224\234\000\342\224\200\000\342\224\200\[\e[0m\]\[\e[38;5;196m\]\000\342\235\260\[\e[0m\]bash_ver:\[\e[38;5;10m\]\v\[\e[0m\]\[\e[38;5;196m\]\000\342\235\261\[\e[0m\]\[\e[38;5;196m\]\000\342\224\201\[\e[0m\]\[\e[38;5;196m\]\000\342\235\260\[\e[0m\]bash_ver_release:\[\e[38;5;10m\]\V\[\e[0m\]\[\e[38;5;196m\]\000\342\235\261\[\e[0m\]\n\[\e[38;5;196m\]\000\342\224\234\000\342\224\200\000\342\224\200\[\e[0m\]\[\e[38;5;196m\]\000\342\235\260\[\e[0m\]cmd#:\[\e[38;5;10m\]\#\[\e[0m\]\[\e[38;5;196m\]\000\342\235\261\[\e[0m\]\[\e[38;5;196m\]\000\342\224\201\[\e[0m\]\[\e[38;5;196m\]\000\342\235\260\[\e[0m\]hist:\[\e[38;5;10m\]\!\[\e[0m\]\[\e[38;5;196m\]\000\342\235\261\[\e[0m\]\[\e[38;5;196m\]\000\342\224\201\[\e[0m\]\[\e[38;5;196m\]\000\342\235\260\[\e[0m\]jobs:\[\e[38;5;10m\]\j\[\e[0m\]\[\e[38;5;196m\]\000\342\235\261\[\e[0m\]\[\e[38;5;196m\]\000\342\224\201\[\e[0m\]\[\e[38;5;196m\]\000\342\235\260\[\e[0m\]shell:\[\e[38;5;10m\]\s\[\e[0m\]\[\e[38;5;196m\]\000\342\235\261\[\e[0m\]\[\e[38;5;196m\]\000\342\224\201\[\e[0m\]\[\e[38;5;196m\]\000\342\235\260\[\e[0m\]term:\[\e[38;5;10m\]\l\[\e[0m\]\[\e[38;5;196m\]\000\342\235\261\[\e[0m\]\n\[\e[38;5;196m\]\000\342\224\234\000\342\224\200\000\342\224\200\[\e[0m\]\[\e[38;5;196m\]\000\342\235\260\[\e[0m\]host:\[\e[38;5;10m\]\h\[\e[0m\]\[\e[38;5;196m\]\000\342\235\261\[\e[0m\]\[\e[38;5;196m\]\000\342\224\201\[\e[0m\]\[\e[38;5;196m\]\000\342\235\260\[\e[0m\]host_long:\[\e[38;5;10m\]\H\[\e[0m\]\[\e[38;5;196m\]\000\342\235\261\[\e[0m\]\n\[\e[38;5;196m\]\000\342\224\234\000\342\224\200\000\342\224\200\[\e[0m\]\[\e[38;5;196m\]\000\342\235\260\[\e[0m\]date_24hrtime:\[\e[38;5;10m\]\d \t\[\e[0m\]\[\e[38;5;196m\]\000\342\235\261\[\e[0m\]\[\e[38;5;196m\]\000\342\224\201\[\e[0m\]\[\e[38;5;196m\]\000\342\235\260\[\e[0m\]date_wmd:\[\e[38;5;10m\]\d\[\e[0m\]\[\e[38;5;196m\]\000\342\235\261\[\e[0m\]\[\e[38;5;196m\]\000\342\224\201\[\e[0m\]\[\e[38;5;196m\]\000\342\235\260\[\e[0m\]12hr_am_pm:\[\e[38;5;10m\]\@\[\e[0m\]\[\e[38;5;196m\]\000\342\235\261\[\e[0m\]\n\[\e[38;5;196m\]\000\342\224\234\000\342\224\200\000\342\224\200\[\e[0m\]\[\e[38;5;196m\]\000\342\235\260\[\e[0m\]12hr_am_pm_sec:\[\e[38;5;10m\]\T\[\e[0m\]\[\e[38;5;196m\]\000\342\235\261\[\e[0m\]\[\e[38;5;196m\]\000\342\224\201\[\e[0m\]\[\e[38;5;196m\]\000\342\235\260\[\e[0m\]time_24hrs:\[\e[38;5;10m\]\t\[\e[0m\]\[\e[38;5;196m\]\000\342\235\261\[\e[0m\]\n\[\e[38;5;196m\]\000\342\224\224\000\342\224\200\000\342\225\274\[\e[0m\] \[\e[38;5;11m\]\$ \[\e[0m\]'
```
![too_many_options.sh](https://raw.githubusercontent.com/shollingsworth/ps1/main/media/dark/too_many_options.sh.png)


### [fire_ice.sh](https://github.com/shollingsworth/ps1/blob/main/src/ps1api/examples/light/fire_ice.sh)
```
export PS1='\[\e[38;5;196m\]\[\e[1m\]\000\342\224\214\000\342\224\200\000\342\224\200\[\e[0m\]\[\e[38;5;196m\]\[\e[1m\]\000\342\235\260\[\e[0m\]$(b_err_code=$?; [[ $b_err_code != 0 ]] && echo "\[\e[38;5;196m\]\000\342\234\230\[\e[0m\]/${b_err_code}" || echo "\[\e[38;5;2m\]\000\342\234\224\[\e[0m\]")\[\e[38;5;196m\]\[\e[1m\]\000\342\235\261\[\e[0m\]\[\e[38;5;196m\]\[\e[1m\]\000\342\224\201\[\e[0m\]\[\e[38;5;196m\]\[\e[1m\]\000\342\235\260\[\e[0m\]\[\e[38;5;33m\]\u\[\e[0m\]\[\e[38;5;0m\]@\[\e[0m\]\[\e[38;5;8m\]\h\[\e[0m\]\[\e[38;5;196m\]\[\e[1m\]\000\342\235\261\[\e[0m\]\[\e[38;5;196m\]\[\e[1m\]\000\342\224\201\[\e[0m\]\[\e[38;5;196m\]\[\e[1m\]\000\342\235\260\[\e[0m\]\[\e[38;5;33m\]$(br=$(git branch 2>/dev/null| grep '"'"'^\*'"'"' | awk '"'"'{print $NF}'"'"'); [[ "${br}" ]] && echo "${br}" || echo "-")\[\e[0m\]\[\e[38;5;196m\]\[\e[1m\]\000\342\235\261\[\e[0m\]\n\[\e[38;5;196m\]\[\e[1m\]\000\342\224\234\000\342\224\200\000\342\224\200\[\e[0m\]\[\e[38;5;196m\]\[\e[1m\]\000\342\235\260\[\e[0m\]\[\e[38;5;15m\]\[\e[48;5;33m\]\w\[\e[0m\]\[\e[38;5;196m\]\[\e[1m\]\000\342\235\261\[\e[0m\]\n\[\e[38;5;196m\]\[\e[1m\]\000\342\224\224\000\342\224\200\000\342\225\274\[\e[0m\] \[\e[38;5;33m\]\$ \[\e[0m\]'
```
![fire_ice.sh](https://raw.githubusercontent.com/shollingsworth/ps1/main/media/light/fire_ice.sh.png)


### [magenta.sh](https://github.com/shollingsworth/ps1/blob/main/src/ps1api/examples/light/magenta.sh)
```
export PS1='\[\e[38;5;21m\]\000\342\224\214\000\342\224\200\000\342\224\200\[\e[0m\]\[\e[38;5;21m\]\000\342\235\260\[\e[0m\]$(b_err_code=$?; [[ $b_err_code != 0 ]] && echo "\[\e[38;5;1m\]\000\342\234\230\[\e[0m\]/${b_err_code}" || echo "\[\e[38;5;10m\]\000\342\234\224\[\e[0m\]")\[\e[38;5;21m\]\000\342\235\261\[\e[0m\]\[\e[38;5;21m\]\000\342\224\201\[\e[0m\]\[\e[38;5;21m\]\000\342\235\260\[\e[0m\]\[\e[38;5;201m\]$(br=$(git branch 2>/dev/null| grep '"'"'^\*'"'"' | awk '"'"'{print $NF}'"'"'); [[ "${br}" ]] && echo "${br}" || echo "-")\[\e[0m\]\[\e[38;5;21m\]\000\342\235\261\[\e[0m\]\n\[\e[38;5;21m\]\000\342\224\234\000\342\224\200\000\342\224\200\[\e[0m\]\[\e[38;5;21m\]\000\342\235\260\[\e[0m\]\[\e[38;5;201m\]\w\[\e[0m\]\[\e[38;5;21m\]\000\342\235\261\[\e[0m\]\n\[\e[38;5;21m\]\000\342\224\224\000\342\224\200\000\342\225\274\[\e[0m\] \[\e[38;5;8m\]\$ \[\e[0m\]'
```
![magenta.sh](https://raw.githubusercontent.com/shollingsworth/ps1/main/media/light/magenta.sh.png)


### [powderpuff.sh](https://github.com/shollingsworth/ps1/blob/main/src/ps1api/examples/light/powderpuff.sh)
```
export PS1='\[\e[38;5;199m\]\[\e[1m\]\000\342\224\214\000\342\224\200\000\342\224\200\[\e[0m\]\[\e[38;5;199m\]\[\e[1m\]\000\342\235\260\[\e[0m\]$(b_err_code=$?; [[ $b_err_code != 0 ]] && echo "\[\e[38;5;196m\]\000\342\234\230\[\e[0m\]/${b_err_code}" || echo "\[\e[38;5;2m\]\000\342\234\224\[\e[0m\]")\[\e[38;5;199m\]\[\e[1m\]\000\342\235\261\[\e[0m\]\[\e[38;5;199m\]\[\e[1m\]\000\342\224\201\[\e[0m\]\[\e[38;5;199m\]\[\e[1m\]\000\342\235\260\[\e[0m\]\[\e[38;5;91m\]\u\[\e[0m\]\[\e[38;5;206m\]@\[\e[0m\]\[\e[38;5;8m\]\h\[\e[0m\]\[\e[38;5;199m\]\[\e[1m\]\000\342\235\261\[\e[0m\]\[\e[38;5;199m\]\[\e[1m\]\000\342\224\201\[\e[0m\]\[\e[38;5;199m\]\[\e[1m\]\000\342\235\260\[\e[0m\]\[\e[38;5;91m\]$(br=$(git branch 2>/dev/null| grep '"'"'^\*'"'"' | awk '"'"'{print $NF}'"'"'); [[ "${br}" ]] && echo "${br}" || echo "-")\[\e[0m\]\[\e[38;5;199m\]\[\e[1m\]\000\342\235\261\[\e[0m\]\n\[\e[38;5;199m\]\[\e[1m\]\000\342\224\234\000\342\224\200\000\342\224\200\[\e[0m\]\[\e[38;5;199m\]\[\e[1m\]\000\342\235\260\[\e[0m\]\[\e[38;5;15m\]\[\e[48;5;91m\]\w\[\e[0m\]\[\e[38;5;199m\]\[\e[1m\]\000\342\235\261\[\e[0m\]\n\[\e[38;5;199m\]\[\e[1m\]\000\342\224\224\000\342\224\200\000\342\225\274\[\e[0m\] \[\e[38;5;91m\]\$ \[\e[0m\]'
```
![powderpuff.sh](https://raw.githubusercontent.com/shollingsworth/ps1/main/media/light/powderpuff.sh.png)


## Other Docs [&#8593;](#toc)
* [Api Docs](https://shollingsworth.github.io/ps1/)
* [Changelog](./CHANGELOG.md)
