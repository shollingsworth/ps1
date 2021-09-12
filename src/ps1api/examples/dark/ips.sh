_ips() {
    {
        echo -ne " "
        tput setaf 7
        hostname -I
        tput sgr0
    } | tr '\n' ' '
}

_shentropy() {
    entropy=$(cat /proc/sys/kernel/random/entropy_avail)
    if [[ "${entropy}" -lt 500 ]]; then
        echo "$(tput setaf 1)✗/${entropy}$(tput sgr0)"
    else
        echo "$(tput setaf 2)✔/${entropy}$(tput sgr0)"
    fi
}

_c1="red_1"
_c2="dodger_blue_1"


PS1="$(
ps1.py \
    custom \
    --set_section_color "${_c1}:bold" \
    --set_fancy_lines \
    --set_ends "❰" "❱" \
    --set_section_delim "━" \
    --set_prompt_color "white" \
    --add_exit_code "✔" "✘" "green" "red_1" \
    --add_custom 'entropy:$(_shentropy)' "" \
    --add_newline \
    --add_git_branch "light_yellow" \
    --add_custom 'ips:$(_ips)' "" \
    --add_newline \
    --add_working_directory "${_c2}" \
    --add_newline \
)"
export PS1
