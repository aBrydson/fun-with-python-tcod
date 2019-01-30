def get_colours_under_mouse(mouse, console):
    (x, y) = (mouse.cx, mouse.cy)

    bg_colour = tuple(console.bg[x,y])

    return bg_colour

def render_tooltip(tooltip_console, root_console, entities, mouse, current_map=None):

    tooltip_console.clear()

    if current_map:
        names_string = get_names_under_mouse(mouse, entities, current_map)

    else:
        names_string = entities

    # Wrap the names to lines and get a count of lines for height of tooltip
    tooltip_lines = textwrap.wrap(names_string, tooltip_console.width - 2)

    y = 1
    for line in tooltip_lines:
        tooltip_console.print_(1, y, line, bg_blend=0)
        y += 1

    # The border
    # The corners of the tooltip box
    x1 = 0
    y1 = 0
    x2 = len(tooltip_lines[0]) + 1
    y2 = len(tooltip_lines) + 1

    tcod.console_put_char(tooltip_console, x1, y1, 218)
    tcod.console_put_char(tooltip_console, x2, y1, 191)
    tcod.console_put_char(tooltip_console, x1, y2, 192)
    tcod.console_put_char(tooltip_console, x2, y2, 217)

    # Lines between the corners
    tooltip_console.vline(x1, y1 + 1, max(len(tooltip_lines), 1))
    tooltip_console.vline(x2, y1 + 1, max(len(tooltip_lines), 1))
    tooltip_console.hline(x1 + 1, y1, max(len(tooltip_lines[0]), 1))
    tooltip_console.hline(x1 + 1, y2, max(len(tooltip_lines[0]), 1))

    if ((mouse.cx+2) + (len(tooltip_lines[0]) + 2)) > root_console.width:
        tooltip_console.blit(root_console,
                            (mouse.cx - 2) - (len(tooltip_lines[0])),
                            mouse.cy, 0, 0, 
                            len(tooltip_lines[0]) + 2, 
                            y2 + 1, 
                            bg_alpha=0.75)
    else:                         
        tooltip_console.blit(root_console, mouse.cx + 2, mouse.cy, 0, 0, len(tooltip_lines[0]) + 2, y2 + 1, bg_alpha=0.75)
