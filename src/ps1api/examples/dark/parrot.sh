export PS1=$(
ps1 \
    custom \
    --set_fancy_lines \
    --set_ends "❰" "❱" \
    --set_section_delim "━" \
    --add_exit_code \
    --add_user_host \
    --add_working_directory \
    --add_newline \
    --add_git_branch \
    --add_newline \

)
