def open_chargen_menu(constants, consoles, world_data):

    tcod.console_flush()

    show_chargen_menu = True
    intro_sequence = False
    show_choice_window = False
    summary_text = None

    rootcon = consoles[0]
    introcon2 = consoles[2]
    tooltipcon = consoles[6]

    key = tcod.Key()
    mouse = tcod.Mouse()

    introcon2.blit(rootcon) 
    chargencon = tcod.console_from_xp('data/Europa.xp')
    tcod.console_set_default_foreground(chargencon, tcod.dark_orange)


    

    for fade in range(1,1024):
        introcon2.blit(rootcon)
        chargencon.blit(rootcon, fg_alpha=fade/1024.0, bg_alpha=fade/1024.0)
        tcod.console_flush()



    while not tcod.console_is_window_closed():

        tcod.sys_check_for_event(tcod.EVENT_KEY_PRESS | tcod.EVENT_MOUSE, key, mouse)

        if show_chargen_menu:
            tcod.console_flush()
            chargencon.blit(rootcon)

            action = input_main_menu_keys(key)
            mouse_action = handle_mouse_input(mouse)

            exit_menu           =   action.get('exit')

            (x, y) = (mouse.cx, mouse.cy)

            bg_colour = get_colours_under_mouse(mouse, rootcon)

            for origin, colour in world_data['origins'].items():
                if bg_colour == colour and not show_choice_window:
                    
                    render_tooltip(tooltipcon, rootcon, origin, mouse, current_map=None)

                    if mouse_action.get('left_click'):
                        summary_text = world_data['origin_summaries'][origin]
                        show_choice_window = True

            if show_choice_window:

                action = input_yes_no_menu_keys(key)

                confirm             =   action.get('Yes')
                deny                =   action.get('No')
                exit_menu           =   action.get('exit')

                if summary_text:
                    message_x = 2
                    message_y = 4
                    message_box(rootcon, summary_text, constants['root_width']-4, constants['root_width'], constants['root_height'], message_x, message_y)

                    choice = 'Is this your desired origin?'

                    yes_no_menu(rootcon, choice, len(choice)+2, constants['root_width'], constants['root_height'])

                if confirm:
                    print('origin confirmed: open main chargen menu')

                elif deny:
                        show_chargen_menu = True
                        show_choice_window = False
                        summary_text = None

                elif exit_menu:
                        show_choice_window = False
                        summary_text = None

            elif exit_menu:
                    show_chargen_menu = False

        else:
            open_main_menu(intro_sequence, constants, consoles, world_data)
