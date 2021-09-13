_shentropy() {
    entropy=$(cat /proc/sys/kernel/random/entropy_avail)
    if [[ "${entropy}" -lt 500 ]]; then
        echo "$(tput setaf 1)✗/${entropy}$(tput sgr0)"
    else
        echo "$(tput setaf 2)✔/${entropy}$(tput sgr0)"
    fi
}


_c1="red_1"
_c2="light_green"

export PS1=$(
ps1 \
    custom \
    --set_fancy_lines \
    --set_ends "❰" "❱" \
    --set_section_delim "━" \
    --set_section_color "${_c1}" \
    \
    --add_exit_code \
    --add_newline \
    \
    --add_custom '$(_shentropy)' "" "entropy" \
    --add_newline \
    \
    --add_git_branch ${_c2} "git" \
    --add_newline \
    \
    --add_user ${_c2} "user" \
    --add_user_host \
    --add_newline \
    \
    --add_working_dir_basename ${_c2} "working_dir_basename" \
    --add_working_directory ${_c2} "working_dir" \
    --add_newline \
    \
    --add_bash_ver ${_c2} "bash_ver" \
    --add_bash_ver_release ${_c2} "bash_ver_release" \
    --add_newline \
    \
    --add_cmd_num ${_c2} "cmd#" \
    --add_hist_num ${_c2} "hist" \
    --add_jobs ${_c2} "jobs" \
    --add_shell_name ${_c2} "shell" \
    --add_term_base ${_c2} "term" \
    --add_newline \
    \
    --add_host ${_c2} "host" \
    --add_host_long ${_c2} "host_long" \
    --add_newline \
    \
    --add_date_time_24hr ${_c2} "date_24hrtime" \
    --add_date_week_month_day ${_c2} "date_wmd" \
    --add_time_12hr_am_pm ${_c2} "12hr_am_pm" \
    --add_newline \
    --add_time_12hr_with_second ${_c2} "12hr_am_pm_sec" \
    --add_time_24 ${_c2} "time_24hrs" \
    --add_newline \
)
