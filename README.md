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
### subcommand listcolors
```
usage: ps1 listcolors [-h] [--filter [FILTER [FILTER ...]]]

optional arguments:
  -h, --help            show this help message and exit
  --filter [FILTER [FILTER ...]], -f [FILTER [FILTER ...]]
                        Filter color values

```


### subcommand template
```
usage: ps1 template [-h] [-t TEMPLATE_NAME] [-l]

optional arguments:
  -h, --help            show this help message and exit
  -t TEMPLATE_NAME, --template_name TEMPLATE_NAME
                        Template Name
  -l, --list            List Templates

```


### subcommand custom
```
usage: ps1 custom [-h] [--add_custom [ADD_CUSTOM [ADD_CUSTOM ...]]] [--add_exit_code [ADD_EXIT_CODE [ADD_EXIT_CODE ...]]]
                        [--add_git_branch [ADD_GIT_BRANCH [ADD_GIT_BRANCH ...]]] [--add_newline [ADD_NEWLINE [ADD_NEWLINE ...]]]
                        [--add_user_host [ADD_USER_HOST [ADD_USER_HOST ...]]]
                        [--add_working_directory [ADD_WORKING_DIRECTORY [ADD_WORKING_DIRECTORY ...]]]
                        [--set_ends [SET_ENDS [SET_ENDS ...]]] [--set_fancy_lines [SET_FANCY_LINES [SET_FANCY_LINES ...]]]
                        [--set_no_color [SET_NO_COLOR [SET_NO_COLOR ...]]]
                        [--set_prompt_color [SET_PROMPT_COLOR [SET_PROMPT_COLOR ...]]]
                        [--set_section_color [SET_SECTION_COLOR [SET_SECTION_COLOR ...]]]
                        [--set_section_delim [SET_SECTION_DELIM [SET_SECTION_DELIM ...]]]

optional arguments:
  -h, --help            show this help message and exit
  --add_custom [ADD_CUSTOM [ADD_CUSTOM ...]]
                        ARGS:value,color
                        Add custom section value/color.
  --add_exit_code [ADD_EXIT_CODE [ADD_EXIT_CODE ...]]
                        ARGS:ok_txt,err_txt,ok_color,err_color
                        Add Exit code indicator to prompt.
  --add_git_branch [ADD_GIT_BRANCH [ADD_GIT_BRANCH ...]]
                        ARGS:color
                        Add git branch to prompt.
  --add_newline [ADD_NEWLINE [ADD_NEWLINE ...]]
                        ARGS:None
                        Insert newline.
  --add_user_host [ADD_USER_HOST [ADD_USER_HOST ...]]
                        ARGS:user_color,at_sym_color,host_color
                        Add User/Host to prompt.
                        ::
                            [user@hostname]-[section2]
                                  ^ add this
  --add_working_directory [ADD_WORKING_DIRECTORY [ADD_WORKING_DIRECTORY ...]]
                        ARGS:color
                        Add Working directory to prompt.
                        ::
                            [user@hostame]─[~/path/i/am/in]
                                             ^ add this
  --set_ends [SET_ENDS [SET_ENDS ...]]
                        ARGS:start,end
                        Set Section start / end values.
                        ::
                            {}
                            {section1}-{section2}
                        
                            []
                            [section1]-[section2]
                        
                            ❰❱
                            ❰section1❱-❰section2❱
  --set_fancy_lines [SET_FANCY_LINES [SET_FANCY_LINES ...]]
                        ARGS:value
                        Set fancy line breaks like the following
                        ::
                            ┌───
                            ├───
                            └──╼
  --set_no_color [SET_NO_COLOR [SET_NO_COLOR ...]]
                        ARGS:value
                        Set terminal to no color.
  --set_prompt_color [SET_PROMPT_COLOR [SET_PROMPT_COLOR ...]]
                        ARGS:color
                        Set prompt color.
                        ::
                            i.e. $ or # depending on user
  --set_section_color [SET_SECTION_COLOR [SET_SECTION_COLOR ...]]
                        ARGS:color
                        Set default section color.
  --set_section_delim [SET_SECTION_DELIM [SET_SECTION_DELIM ...]]
                        ARGS:delim
                        Set section separator.
                        ::
                            i.e. [section1]-[section2]
                                           ^ separator

```


### subcommand examples
```
usage: ps1 examples [-h]

optional arguments:
  -h, --help  show this help message and exit

```


## Examples [&#8593;](#toc)
### [entropy.sh](https://github.com/shollingsworth/ps1/blob/main/src/ps1api/examples/dark/entropy.sh)
![entropy.sh](https://raw.githubusercontent.com/shollingsworth/ps1/main/media/dark/entropy.sh.png)


### [parrot.sh](https://github.com/shollingsworth/ps1/blob/main/src/ps1api/examples/dark/parrot.sh)
![parrot.sh](https://raw.githubusercontent.com/shollingsworth/ps1/main/media/dark/parrot.sh.png)


### [skulls.sh](https://github.com/shollingsworth/ps1/blob/main/src/ps1api/examples/dark/skulls.sh)
![skulls.sh](https://raw.githubusercontent.com/shollingsworth/ps1/main/media/dark/skulls.sh.png)


### [purplegoblin.sh](https://github.com/shollingsworth/ps1/blob/main/src/ps1api/examples/dark/purplegoblin.sh)
![purplegoblin.sh](https://raw.githubusercontent.com/shollingsworth/ps1/main/media/dark/purplegoblin.sh.png)


### [plainjane.sh](https://github.com/shollingsworth/ps1/blob/main/src/ps1api/examples/dark/plainjane.sh)
![plainjane.sh](https://raw.githubusercontent.com/shollingsworth/ps1/main/media/dark/plainjane.sh.png)


### [greenguy.sh](https://github.com/shollingsworth/ps1/blob/main/src/ps1api/examples/dark/greenguy.sh)
![greenguy.sh](https://raw.githubusercontent.com/shollingsworth/ps1/main/media/dark/greenguy.sh.png)


### [filecount.sh](https://github.com/shollingsworth/ps1/blob/main/src/ps1api/examples/dark/filecount.sh)
![filecount.sh](https://raw.githubusercontent.com/shollingsworth/ps1/main/media/dark/filecount.sh.png)


### [magenta.sh](https://github.com/shollingsworth/ps1/blob/main/src/ps1api/examples/light/magenta.sh)
![magenta.sh](https://raw.githubusercontent.com/shollingsworth/ps1/main/media/light/magenta.sh.png)


### [powderpuff.sh](https://github.com/shollingsworth/ps1/blob/main/src/ps1api/examples/light/powderpuff.sh)
![powderpuff.sh](https://raw.githubusercontent.com/shollingsworth/ps1/main/media/light/powderpuff.sh.png)


### [fire_ice.sh](https://github.com/shollingsworth/ps1/blob/main/src/ps1api/examples/light/fire_ice.sh)
![fire_ice.sh](https://raw.githubusercontent.com/shollingsworth/ps1/main/media/light/fire_ice.sh.png)


## Other Docs [&#8593;](#toc)
* [Api Docs](https://shollingsworth.github.io/ps1/)
* [Changelog](./CHANGELOG.md)
