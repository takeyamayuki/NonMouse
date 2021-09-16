from pyhooked import Hook, KeyboardEvent, MouseEvent


def handle_events(args):
    if isinstance(args, KeyboardEvent):
        print(args.key_code, args.current_key, args.event_type)

    if isinstance(args, MouseEvent):
        print(args.mouse_x, args.mouse_y)

hk = Hook()  # make a new instance of PyHooked
hk.handler = handle_events  # add a new shortcut ctrl+a, or triggered on mouseover of (300,400)
hk.hook()  # hook into the events, and listen to the presses