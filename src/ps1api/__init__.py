#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PS1 Prompt module."""
from colored import fg, bg, attr, names
from pathlib import Path
import itertools
import re


def iter_examples():
    """Iterate through example files."""

    def _iterfiles(p: Path):
        for i in p.iterdir():
            if i.is_dir():
                yield from _iterfiles(i)
            else:
                yield i

    exdir = Path(__file__).parent.joinpath("examples")
    for i in _iterfiles(exdir):
        cont = i.read_text()
        yield i, cont


class Base(object):
    """Base PS1 Building object."""

    USER = r"\u"
    """PS1 user expansion value."""

    HOST = r"\h"
    """PS1 host expansion value."""

    HOST_LONG = r"\H"
    """PS1 host expansion value."""

    WORKING_DIR = r"\w"
    """PS1 working directory expansion value."""

    PROMPT = r"\$ "
    """PS1 prompt for regular user / root user."""

    TERM_BASE = r"\l"
    """The basename of the shell's terminal device name."""

    JOBS = r"\j"
    """The number of jobs currently managed by the shell."""

    HIST_NUM = r"\!"
    """History count."""

    CMD_NUM = r"\#"
    """Number of commands this terminal has run."""

    DATE_WEEK_MONTH_DAY = r"\d"
    """Date week month day."""

    SHELL_NAME = r"\s"
    """The name of the shell, the basename of $0 (the portion following the final slash)."""

    TIME_24 = r"\t"
    """The time, in 24-hour HH:MM:SS format."""

    TIME_12HR_W_SECOND = r"\T"
    """The time, in 12-hour HH:MM:SS format."""

    TIME_12HR_AM_PM = r"\@"
    """The time, in 12-hour am/pm format."""

    BASH_VER = r"\v"
    """The version of Bash (e.g., 2.00)."""
    BASH_VER_RELEASE = r"\V"
    """The release of Bash, version + patchlevel (e.g., 2.00.0)."""

    WORKING_DIR_BASENAME = r"\W"
    """The basename of $PWD."""

    def __init__(self):
        """Initialize class."""
        self.set_section_color()
        self.set_ends()
        self.set_prompt_color()
        self.set_section_delim()
        self.fancy_lines = False
        """Turn on Fancy lines."""
        self.set_no_color(False)
        self.sections = []
        """Sections list."""

        self.build_template()

    def _strip_color(self, value):
        """Strip color from output."""
        ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")
        return ansi_escape.sub("", value)

    def set_no_color(self, value=True):
        """Set terminal to no color."""
        self.no_color = value
        """Disable color from PS1 prompt."""

    def set_fancy_lines(self):
        """
        Set fancy line breaks like the following
        ::
            ┌───
            ├───
            └──╼
        """
        self.fancy_lines = True

    def set_section_delim(self, delim="-"):
        """
        Set section separator.
        ::
            i.e. [section1]-[section2]
                           ^ separator
        """
        self.delim = delim
        """Section delimiter."""

    def set_section_color(self, color="red_1"):
        """Set default section color."""
        self.section_color = color
        """Delim and prefix/suffix color."""

    def set_prompt_color(self, color="light_yellow"):
        """
        Set prompt color.
        ::
            i.e. $ or # depending on user
        """
        self.prompt_color = color
        """PS1 Prompt $/# color."""

    @classmethod
    def color(cls, cval: str, txt, escape=True):
        """Abstracted color class."""
        fg_name = None
        bg_name = None
        attrs = []
        if "/" in cval and ":" in cval:
            fg_name, work = cval.split("/")
            arr = work.split(":")
            attrs = arr[1:]
            bg_name = arr[0]
        elif "/" in cval:
            fg_name, bg_name = cval.split("/")
        elif ":" in cval:
            arr = cval.split(":")
            fg_name = arr[0]
            attrs = arr[1:]
        else:
            fg_name = cval

        # enclose color codes in escaped bracketed to prevent weirdness at the prompt
        # https://superuser.com/a/609940
        _fg = fg(fg_name) if fg_name else ""
        _bg = bg(bg_name) if bg_name else ""
        attr_str = "".join([attr(attr_name) for attr_name in attrs])
        end_val = attr("reset")
        if escape:
            _fg = "\\[%s\\]" % _fg if _fg else ""
            _bg = "\\[%s\\]" % _bg if _bg else ""
            attr_str = "\\[%s\\]" % attr_str if attr_str else ""
            end_val = "\\[%s\\]" % end_val
        color_v = "".join([_fg, _bg, attr_str])
        retval = f"{color_v}{txt}{end_val}"
        return retval

    def build_template(self):
        """Build template (if defined in subclass)."""
        pass

    def _sammy(self, value):
        """Sandwhich section between separators."""
        return "".join(
            [
                self.color(self.section_color, self.section_prefix),
                value,
                self.color(self.section_color, self.section_suffix),
            ]
        )

    def set_ends(self, start="[", end="]"):
        """
        Set Section start / end values.
        ::
            {}
            {section1}-{section2}

            []
            [section1]-[section2]

            ❰❱
            ❰section1❱-❰section2❱
        """

        def _repl_brackets(val):
            """Replace brackets with octal to avoid confusion."""
            return val.replace("]", r"\135").replace("[", r"\133")

        start, end = map(_repl_brackets, [start, end])
        self.section_prefix = start
        """Section prefix."""
        self.section_suffix = end
        """Section suffix."""
        return self

    def add_custom(self, value: str, color: str, title: str = None):
        """Add custom section value/color."""
        self.sections.append((value, color, title))
        return self

    def add_newline(self):
        """Insert newline."""
        self.sections.append(("__NL__", None, None))
        return self

    def add_user_host(
        self,
        user_color: str = "grey_62",
        at_sym_color: str = "light_yellow",
        host_color: str = "light_blue",
    ):
        """
        Add User/Host to prompt.
        ::
            [user@hostname]-[section2]
                  ^ add this
        """
        sect = []
        sect.append(self.color(user_color, self.USER))
        sect.append(self.color(at_sym_color, "@"))
        sect.append(self.color(host_color, self.HOST))
        val = "".join(sect)
        self.sections.append((val, None, None))
        return self

    def add_working_directory(
        self,
        color: str = "light_green",
        title: str = "",
    ):
        """
        Add Working directory to prompt.
        ::
            [user@hostame]─[~/path/i/am/in]
                             ^ add this
        """
        self.sections.append((self.WORKING_DIR, color, title))
        return self

    def add_git_branch(
        self,
        color: str = "light_yellow",
        title: str = "",
    ):
        """
        Add git branch to prompt.
        """
        val = r"""$(br=$(git branch 2>/dev/null| grep '^\*' | awk '{print $NF}'); [[ "${br}" ]] && echo "${br}" || echo "-")"""
        self.sections.append((val, color, title))
        return self

    def add_exit_code(
        self,
        # ok_txt: str = "o",
        # err_txt: str = "x",
        ok_txt: str = "✔",
        err_txt: str = "✘",
        ok_color: str = "light_green",
        err_color: str = "red_1",
        title: str = "",
    ):
        """Add Exit code indicator to prompt."""
        ok = self.color(ok_color, ok_txt)
        err = self.color(err_color, err_txt)
        val = f'$(b_err_code=$?; [[ $b_err_code != 0 ]] && echo "{err}/${{b_err_code}}" || echo "{ok}")'
        self.sections.append((val, None, title))
        return self

    def add_user(
        self,
        color: str = "",
        title: str = "",
    ):
        """
        Add PS1 user expansion value.
        """
        self.sections.append((self.USER, color, title))
        return self

    def add_host(
        self,
        color: str = "",
        title: str = "",
    ):
        """
        Add PS1 host expansion value.
        """
        self.sections.append((self.HOST, color, title))
        return self

    def add_host_long(
        self,
        color: str = "",
        title: str = "",
    ):
        """
        Add PS1 host expansion value.
        """
        self.sections.append((self.HOST_LONG, color, title))
        return self

    def add_term_base(
        self,
        color: str = "",
        title: str = "",
    ):
        """
        Add The basename of the shell's terminal device name.
        """
        self.sections.append((self.TERM_BASE, color, title))
        return self

    def add_jobs(
        self,
        color: str = "",
        title: str = "",
    ):
        """
        Add The number of jobs currently managed by the shell.
        """
        self.sections.append((self.JOBS, color, title))
        return self

    def add_hist_num(
        self,
        color: str = "",
        title: str = "",
    ):
        """
        Add History count.
        """
        self.sections.append((self.HIST_NUM, color, title))
        return self

    def add_cmd_num(
        self,
        color: str = "",
        title: str = "",
    ):
        """
        Add Number of commands this terminal has run.
        """
        self.sections.append((self.CMD_NUM, color, title))
        return self

    def add_date_week_month_day(
        self,
        color: str = "",
        title: str = "",
    ):
        """
        Add Date week month day.
        ::
            Mon Sep 13
        """
        self.sections.append((self.DATE_WEEK_MONTH_DAY, color, title))
        return self

    def add_date_time_24hr(
        self,
        color: str = "",
        title: str = "",
    ):
        """
        Add the date/time, in 24-hour HH:MM:SS format.
        ::
            Mon Sep 13 10:28:40
        """
        val = " ".join([self.DATE_WEEK_MONTH_DAY, self.TIME_24])
        self.sections.append((val, color, title))
        return self

    def add_shell_name(
        self,
        color: str = "",
        title: str = "",
    ):
        """
        Add The name of the shell, the basename of $0 (the portion following the final slash).
        """
        self.sections.append((self.SHELL_NAME, color, title))
        return self

    def add_time_24(
        self,
        color: str = "",
        title: str = "",
    ):
        """
        Add The time, in 24-hour HH:MM:SS format.
        ::
            10:28:40
        """
        self.sections.append((self.TIME_24, color, title))
        return self

    def add_time_12hr_with_second(
        self,
        color: str = "",
        title: str = "",
    ):
        """
        Add The time, in 12-hour HH:MM:SS format.
        ::
            10:28:40
        """
        self.sections.append((self.TIME_12HR_W_SECOND, color, title))
        return self

    def add_time_12hr_am_pm(
        self,
        color: str = "",
        title: str = "",
    ):
        """
        Add The time, in 12-hour am/pm format.
        ::
            10:28 AM
        """
        self.sections.append((self.TIME_12HR_AM_PM, color, title))
        return self

    def add_bash_ver(
        self,
        color: str = "",
        title: str = "",
    ):
        """
        Add The version of Bash (e.g., 2.00).
        """
        self.sections.append((self.BASH_VER, color, title))
        return self

    def add_bash_ver_release(
        self,
        color: str = "",
        title: str = "",
    ):
        """
        Add The release of Bash, version + patchlevel (e.g., 2.00.0).
        """
        self.sections.append((self.BASH_VER_RELEASE, color, title))
        return self

    def add_working_dir_basename(
        self,
        color: str = "",
        title: str = "",
    ):
        """
        Add The basename of $PWD.
        """
        self.sections.append((self.WORKING_DIR_BASENAME, color, title))
        return self

    def output(self):
        """Output / export PS1 value."""
        sep = self.color(self.section_color, self.delim)
        mod_lines = []
        for val, color, title in self.sections:
            if val == "__NL__":
                mod_lines.append(val)
            elif not color:
                if title:
                    ival = f"{title}:{val}"
                else:
                    ival = val
                mod_lines.append(self._sammy(ival))
            else:
                if title:
                    ival = f"{title}:{self.color(color, val)}"
                else:
                    ival = self.color(color, val)
                mod_lines.append(self._sammy(ival))

        f_start = self.color(self.section_color, "┌──")
        f_mid = self.color(self.section_color, "├──")
        f_last = self.color(self.section_color, "└─╼")

        lines = []
        sects = []
        for i in mod_lines:
            if i == "__NL__":
                lines.append(sep.join(sects))
                sects = []
            else:
                sects.append(i)
        lines.append(sep.join(sects))
        retval = []
        for idx, i in enumerate(lines):
            if idx == 0:
                retval.append(f"{f_start}{i}" if self.fancy_lines else i)
            elif idx == len(lines) - 1:
                retval.append(f"{f_last}{i}" if self.fancy_lines else i)
            else:
                retval.append(f"{f_mid}{i}" if self.fancy_lines else i)
        retval = "\n".join(retval)
        pad = " "
        pval = self.color(self.prompt_color, self.PROMPT)
        retval = f"{retval}{pad}{pval}"

        if self.no_color:
            return self._strip_color(retval).replace(r"\[\]", "")
        output = "\n".join(i.lstrip() for i in retval.splitlines())
        output = output.replace("\x1b", r"\e").replace("\n", r"\n")

        # Convert UTF-8 values to Octal bash escape sequences
        def _uniconv(val):
            i = ord(val)
            if i < 256:
                return val
            else:
                enc = val.encode()
                while len(enc) % 4 != 0:
                    enc = b"\0" + enc
                return "\\%s" % "\\".join([f"{i:o}".zfill(3) for i in enc])

        output = "".join(map(_uniconv, output))
        return output


class Parrot(Base):
    """Parrot Template."""

    def build_template(self):
        """Build template."""
        self.set_fancy_lines()
        self.add_exit_code()
        self.add_user_host()
        self.add_working_directory()
        self.add_newline()


class ParrotGit(Base):
    """Parrot git template."""

    def build_template(self):
        """Build template."""
        self.set_fancy_lines()
        self.set_ends("[", "]")
        self.set_section_delim("-")
        self.add_exit_code()
        self.add_user_host()
        self.add_working_directory()
        self.add_newline()
        self.add_git_branch()
        self.add_newline()


def get_color_codes(*filter_vals):
    """Show Color Codes."""

    def split_len(arr):
        """Split a iterable into all length variations."""
        # chunk a list into every length combination
        vals = set()
        for i in itertools.product(arr, repeat=len(arr)):
            vals.add(tuple(set(i)))
        for i in sorted(vals):
            yield list(i)

    attr_inc = [
        "bold",
    ]

    attr_combos = list(split_len(attr_inc))

    for i in names:
        code = i.lower()
        if all([m in code for m in filter_vals]):
            yield Base().color(code, code, False)

    for bg in names:
        bg = bg.lower()
        for i in names:
            i = i.lower()
            code = f"{i}/{bg}"
            if all([m in code for m in filter_vals]):
                yield Base().color(code, code, False)

    for k in attr_combos:
        for bg in ["white", "black"]:
            for i in names:
                i = i.lower()
                akey = ":".join(k)
                code = f"{i}/{bg}:{akey}"
                if all([m in code for m in filter_vals]):
                    yield Base().color(code, code, False)
