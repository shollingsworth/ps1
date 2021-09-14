_c1="red_1"
_c2="dodger_blue_1"
_c3="red_1"
PS1=$(
ps1 \
    custom \
    --set_ends "[" "]" \
    --set_delim_color "grey_15/black:bold" \
    --set_section_delim "∔" \
    --set_section_color "grey_39/black:bold" \
    --set_prompt_color "white" \
    --add_exit_code "✔" "✘" "green" "red_1" "" \
    --add_date_time_24hr "green" \
    --add_jobs "$_c3" "jobs" \
    --add_cmd_num "$_c3" "cmd#" \
    --add_newline \
    --add_working_directory "${_c2}" "" \
    --add_newline \
)
export PS1
