    import shlex

    # args = parser.parse_args()
    # args = parser.parse_args(["-l"])
    argset = " ".join(
        [
            #  "template",
            #  "parrotgit",
            # "list",
            #  "custom",
            #  "--add_custom 'test' 'yellow'",
            #  "--add_custom 'blarg' 'yellow'",
            #  "--set_no_color",
            #  "--add_exit_code",
            #  "--add_user_host",
            #  "--add_working_directory",
            #  "--add_newline",
            #  "--add_git_branch",
            #  "--add_newline",
            #  "--set_ends '[' ']'",
            #  "--set_fancy_lines",
        ]
    )
    args = parser.parse_args()
    args = parser.parse_args(shlex.split(argset))
    arg_vals = [i for i in dir(args) if not i.startswith("_")]
    if not arg_vals:
        parser.print_help()
        raise SystemExit()
    # args = parser.parse_args(["-h"])
    args.func(args)
