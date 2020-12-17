from datetime import datetime as dt


class log:
    def timestamp(self):
        now = dt.now()
        now = str(now)
        now = '[@' + now + ']: '
        return now
    def msg(msg, print_msg=False):
        message = str(log.timestamp()) + msg
        if print_msg == True:
            print(str(log.timestamp()), msg)
        return message
class errors:
    def not_specified(resource=None, level='Warning'):
        message = f'{level}: No {resource} has been specified.'
        log.msg(msg=message, print_msg=True)
        return message