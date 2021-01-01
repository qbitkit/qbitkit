from datetime import datetime as dt


class log:
    def timestamp(self):
        """Returns the current time and date with lots of precision."""
        now = dt.now()
        now = str(now)
        now = '[@' + now + ']: '
        return now
    def msg(msg=None,
            print_msg=False):
        """Attaches a timestamp to a specified message, and prints the message if specified. Returns formatted message.

        Keyword arguments:
        msg -- the message you would like to prepend a timestamp to and return and optionally print. (default None)
        print_msg -- specify whether or not to print the message in addition to returning it as usual. (default False)"""
        message = str(log.timestamp()) + msg
        if print_msg == True:
            print(str(log.timestamp()), msg)
        return message
class errors:
    def not_specified(resource=None,
                      level='Warning'):
        """Throw an error warning the user that a specified resource has not been specified.

        Keyword arguments:
        resource -- name of resource to use in error message. (default None)
        level -- string with desired warning level (default 'Warning')"""
        message = f'{level}: No {resource} has been specified.'
        log.msg(msg=message, print_msg=True)
        return message
    def support_status(feature_state='experimental',
                       resource_name='this qbitkit feature',
                       additional_notes=None):
        """Generate a warning based on specified keyword arguments that warns users that a certain feature is at a certain support stage.

        Keyword arguments:
        feature_state -- The state of the feature, such as experimental or beta. (default 'experimental')
        resource_name -- The name of the feature (resource) to display the feature state of. (default 'this qbitkit feature')
        additional_notes -- Tack on a note to the end of the warning (default None)"""
        message = f"Support for {resource_name} is still in the '{feature_state}' stage. Please use with caution. {additional_notes}"
        log.msg(msg=message,
                print_msg=True)
        return message