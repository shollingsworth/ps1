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
# shellcheck disable=SC2016
PS1=$(
ps1 \
    custom \
    --set_section_delim "" \
    --set_section_color "${_c1}:bold" \
    --set_prompt_color "white" \
    --add_exit_code "✔" "✘" "green" "red_1" "" \
    --add_custom '$(_shentropy)' "" "entropy" \
    --add_date_time_24hr "green" "" \
    --add_jobs "red_1" "jobs" \
    --add_cmd_num "red_1" "cmd#" \
    --add_newline \
    --add_working_directory "${_c2}" "" \
    --add_git_branch "light_yellow" "" \
    --add_newline \
)
export PS1
