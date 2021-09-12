_fcount() {
    timeout .1 find -type f | wc -l 
}

_dirfilesize() {
    timeout .1 du -sh | awk '{print $1}'
}

# FWIW  this is probably a terrable idea, but it demonstrates how you can
# customize different function calls in your prompt

export PS1=$(
ps1 \
    custom \
    --set_ends "❰" "❱" \
    --set_section_delim "━" \
    --set_fancy_lines \
    --set_section_color "light_green" \
    --set_prompt_color "light_green" \
    \
    --add_exit_code \
    --add_git_branch \
    --add_newline \
    --add_custom 'fcnt:$(_fcount)' "red_1" \
    --add_custom 'fsize:$(_dirfilesize)' "magenta" \
    --add_newline \
    --add_working_directory "red_1" \
    --add_user_host \

)
