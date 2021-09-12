_randstr() {
    tr -dc A-Za-z0-9 </dev/urandom | head -c 13 ; echo ''
}

export PS1=$(
ps1 \
    custom \
    --add_exit_code \
    --add_user_host "grey_66" "white" "grey_66" \
    --add_working_directory "grey_27:bold" \
    --add_newline \
    --add_git_branch "red_1" \
    --add_custom 'rando_str:$(_randstr)' "black/grey_27" \
    --add_newline \
    --set_ends "❰" "❱" \
    --set_section_delim "💀" \
    --set_fancy_lines \
    --set_section_color "white:bold" \
    --set_prompt_color "light_green" \
)
