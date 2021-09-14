_shentropy() {
    entropy=$(cat /proc/sys/kernel/random/entropy_avail)
    if [[ "${entropy}" -lt 500 ]]; then
        echo "$(tput setaf 1)x/${entropy}$(tput sgr0)"
    else
        echo "$(tput setaf 2)+/${entropy}$(tput sgr0)"
    fi
}

# shellcheck disable=SC2016
PS1=$(
ps1 \
    custom \
    --set_ends "[" "]" \
    --set_section_delim "" \
    --add_exit_code "+" "x" \
    --add_custom '$(_shentropy)' "" "entropy" \
    --add_git_branch \
    --add_newline \
    --add_working_directory \
    --add_newline \
)
export PS1
