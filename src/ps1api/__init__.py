#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PS1 Prompt module."""
from colored import fg, bg, attr, names
import os
import itertools


class Base(object):
    USER = r"\u"
    HOST = r"\h"
    WORKING_DIR = r"\w"
    PROMPT = "$ " if os.getuid() != 0 else "# "

    def __init__(self):
        self.section_color = "red_1"
        self.prompt_color = "light_yellow"
        self.sections = []
        self.delim = "-"
        self.section_prefix = "["
        self.section_suffix = "]"
        self.fancy_lines = False
        self.build_template()

    @property
    def sep_txt(self):
        return self.color(self.section_color, self.delim)

    @classmethod
    def color(cls, cval: str, txt):
        fg_name = None
        bg_name = None
        attrs = []
        if "/" in cval and ":" in cval:
            fg_name, work = cval.split("/")
            arr = work.split(":")
            attrs = arr[1:]
            bg_name = arr[0]
            _fg = fg(fg_name)
            _bg = bg(bg_name)
        elif "/" in cval:
            fg_name, bg_name = cval.split("/")
        elif ":" in cval:
            arr = cval.split(":")
            fg_name = arr[0]
            attrs = arr[1:]
        else:
            fg_name = cval

        _fg = fg(fg_name)
        _bg = bg(bg_name) if bg_name else ""
        _bg = bg(bg_name) if bg_name is not None else ""
        attr_str = "".join([attr(attr_name) for attr_name in attrs])
        return f"{_fg}{_bg}{attr_str}{txt}{attr(0)}"

    def build_template(self):
        """Build template (if defined in subclass)."""
        pass

    def _sammy(self, value):
        return "".join(
            [
                self.color(self.section_color, self.section_prefix),
                value,
                self.color(self.section_color, self.section_suffix),
            ]
        )

    def set_ends(self, start, end):
        """Set Section start / end values."""
        self.section_prefix = start
        self.section_suffix = end
        return self

    def add_custom(self, value: str, color: str, position=None):
        """Add custom section value."""
        if position is None:
            self.sections.append(self._sammy(self.color(color, value)))
        else:
            self.sections.insert(position, self._sammy(self.color(color, value)))
        return self

    def add_newline(self, position=None):
        if position is None:
            self.sections.append("__NL__")
        else:
            self.sections.insert(position, "__NL__")
        return self

    def add_user_host(
        self,
        user_color: str = "grey_62",
        at_sym_color: str = "light_yellow",
        host_color: str = "light_blue",
        position=None,
    ):
        """Add User/Host to prompt."""
        sect = []
        sect.append(self.color(user_color, self.USER))
        sect.append(self.color(at_sym_color, "@"))
        sect.append(self.color(host_color, self.HOST))
        val = self._sammy("".join(sect))
        if position is None:
            self.sections.append(val)
        else:
            self.sections.insert(position, val)
        return self

    def add_working_directory(
        self,
        color: str = "light_green",
        position=None,
    ):
        """Add Working directory to prompt."""
        val = self._sammy(self.color(color, self.WORKING_DIR))
        if position is None:
            self.sections.append(val)
        else:
            self.sections.insert(position, val)
        return self

    def add_git_branch(self, color: str = "light_yellow", position=None):
        """Add git branch."""
        val = self._sammy(
            self.color(
                color,
                r"""$(br=$(git branch 2>/dev/null| grep '^\*' | awk '{print $NF}'); [[ "${br}" ]] && echo "${br}" || echo "-")""",
            )
        )
        if position is None:
            self.sections.append(val)
        else:
            self.sections.insert(position, val)
        return self

    def add_exit_code(
        self,
        ok_txt: str = "✔",
        err_txt: str = "✘",
        ok_color: str = "light_green",
        err_color: str = "red_1",
        position=None,
    ):
        ok = self.color(ok_color, ok_txt)
        err = self.color(err_color, err_txt)
        val = self._sammy(
            f'$(err=$?; [[ $err != 0 ]] && echo "{err}/${{err}}" || echo "{ok}")'
        )
        if position is None:
            self.sections.append(val)
        else:
            self.sections.insert(position, val)
        return self

    def output(self):
        lines = self.sep_txt.join(self.sections)

        f_start = self.color(self.section_color, "┌──")
        f_mid = self.color(self.section_color, "├──")
        f_last = self.color(self.section_color, "└─╼")

        lines = lines.replace(
            f"{self.sep_txt}__NL__{self.sep_txt}{self.color(self.section_color,self.section_prefix)}",
            "\n",
        )
        lines = lines.replace(
            f"{self.color(self.section_color,self.delim)}__NL__",
            "\n",
        )
        pad = " " if self.fancy_lines else ""
        lines += pad + self.color(self.prompt_color, self.PROMPT)
        retval = []
        spl = lines.splitlines()
        for idx, i in enumerate(spl):
            if idx == 0:
                retval.append(f"{f_start}{i}" if self.fancy_lines else i)
            elif idx == len(spl) - 1:
                retval.append(f"{f_last}{i}" if self.fancy_lines else i)
            else:
                if i:
                    pref = self.color(self.section_color, self.section_prefix)
                    retval.append(
                        f"{f_mid}{pref}{i}" if self.fancy_lines else f"{pref}{i}"
                    )
                else:
                    retval.append(f"{f_mid}{i}" if self.fancy_lines else i)

        return "\n".join(retval)


class Parrot(Base):
    def build_template(self):
        self.add_exit_code()
        self.add_user_host()
        self.add_working_directory()
        self.add_newline()


class ParrotGit(Base):
    def build_template(self):
        self.set_ends("❰", "❱")
        self.delim = "━"
        self.add_exit_code()
        self.add_user_host()
        self.add_working_directory()
        self.add_newline()
        self.add_git_branch()
        self.add_newline()


def show_color_codes():
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
        "underlined",
    ]

    attr_combos = list(split_len(attr_inc))

    bg_colors = [
        "black",
        "white",
        "red_1",
        "light_yellow",
    ]

    for i in names:
        section = []
        i = i.lower()
        section.append(Base().color(i, i))
        for k in attr_combos:
            akey = ":".join(k)
            code = f"{i}:{akey}"
            section.append(Base.color(code, code))
        for z in bg_colors:
            code = f"{i}/{z}"
            section.append(Base.color(code, code))
            for k in attr_combos:
                akey = ":".join(k)
                code = f"{i}/{z}:{akey}"
                section.append(Base.color(code, code))
        section.append("---")
        print("\n".join(section))
