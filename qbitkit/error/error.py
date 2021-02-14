from datetime import datetime as __dt__


class Log:
    def timestamp(self=None):
        """Returns the current time and date with lots of precision.

        Args:
            self(NoneType): unused parameter that does absolutely nothing. (default None)
        Returns:
            str: string describing the current time and date."""
        now = __dt__.now()
        now = str(now)
        now = '[@' + now + ']: '
        return now
    def msg(msg=None,
            print_msg=False):
        """Attaches a timestamp to a specified message, and prints the message if specified. Returns formatted message.

        Args:
            msg (str): the message you would like to prepend a timestamp to and return and optionally print. (default None)
            print_msg (str): specify whether or not to print the message in addition to returning it as usual. (default False)
        Returns:
            str: timestamped and formatted message"""
        message = str(Log.timestamp()) + msg
        if print_msg is True:
            print(str(Log.timestamp()), msg)
        return message


class Errors:
    def not_specified(resource=None,
                      level='Warning'):
        """Throw an error warning the user that a specified resource has not been specified.

        Args:
            resource (str): name of resource to use in error message. (default None)
            level (str): string with desired warning level (default 'Warning')"""
        message = f'{level}: No {resource} has been specified.'
        Log.msg(msg=message, print_msg=True)
        return message

    def support_status(feature_state='experimental',
                       resource_name='this qbitkit feature',
                       additional_notes=None):
        """Generate a warning based on specified keyword arguments that warns users that a certain feature is at a certain support stage.

        Args:
            feature_state (str): The state of the feature, such as experimental or beta. (default 'experimental')
            resource_name (str): The name of the feature (resource) to display the feature state of. (default 'this qbitkit feature')
            additional_notes (str): Tack on a note to the end of the warning (default None)
        Returns:
            str: the generated error message based on specified keyword arguments."""
        if additional_notes is None:
            notes = ''
        else:
            notes = additional_notes
        message = f"Support for {resource_name} is now in the '{feature_state}' stage. Please use with caution. {notes}"
        Log.msg(msg=message,
                print_msg=True)
        return message
