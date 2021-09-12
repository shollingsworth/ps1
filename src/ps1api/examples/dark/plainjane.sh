export PS1=$(
ps1 \
    custom \
    --set_no_color \
    --add_exit_code \
    --add_working_directory \
    --set_ends " " " " \
    --set_section_delim " " \
)
