import re


# TODO: write test
class BaseRegexp:

    def check_fullmatch(self, pattern: str, s: str) -> bool:
        if re.fullmatch(pattern=pattern, string=s):
            return True
        return False


class ManualVersionCheck(BaseRegexp):
    regex = '(?:[0-9][0-9])\.(?:[0-9][1-9])'


class ManualDateCheck(BaseRegexp):
    regex = '(?:0[1-9]|[12][0-9]|3[01])-(?:0[1-9]|1[0-2])-(?:20[12345][0-9])'
