export PS1="$(ps1 \
    custom \
    --add_exit_code \
    --add_user_host \
    --add_working_directory \
    --add_newline \
    --add_git_branch \
    --add_newline \
    --set_ends "❰" "❱" \
    --set_section_delim "━" \
    --set_fancy_lines \
    --set_section_color "magenta" \
    --set_prompt_color "light_green" \
)"
