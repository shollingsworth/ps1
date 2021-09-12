_c1="deep_pink_1b"
_c2="dark_magenta_2"
_c4="hot_pink_1b"
_c5="dark_gray"
export PS1=$(
ps1 \
    custom \
    --set_section_color "${_c1}:bold" \
    --set_fancy_lines \
    --set_ends "❰" "❱" \
    --set_section_delim "━" \
    --set_prompt_color "${_c2}" \
    --add_exit_code "✔" "✘" "green" "red_1" \
    --add_user_host "${_c2}" "${_c4}" "${_c5}" \
    --add_git_branch "${_c2}" \
    --add_newline \
    --add_working_directory "white/${_c2}" \
    --add_newline \
)
