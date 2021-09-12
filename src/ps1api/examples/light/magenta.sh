export PS1=$(
ps1 \
    custom \
    --set_section_color "blue_1" \
    --set_fancy_lines \
    --set_ends "❰" "❱" \
    --set_section_delim "━" \
    --set_prompt_color "dark_gray" \
    --add_exit_code "✔" "✘" "light_green" "red" \
    --add_git_branch "magenta_1" \
    --add_newline \
    --add_working_directory "magenta_1" \
    --add_newline \
)
