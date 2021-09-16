import Cocoa
def evthandler(event):
    pass # this is where you do stuff; see NSEvent documentation for event
observer = Cocoa.NSEvent.addGlobalMonitorForEventsMatchingMask_handler_(NSKeyDown, evthandler)
# when you're done
Cocoa.NSEvent.removeMonitor_(observer)