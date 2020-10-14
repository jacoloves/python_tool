#! /usr/bin/env python

import re

class iosParser:

    def iso_parser(target_str):
        result_str = target_str.replace('PT', '')
        result_str = result_str.replace('H', ':')
        result_str = result_str.replace('M', ':')
        result_str = result_str.replace('S', '')


        if not re.search('S', target_str):
            result_str = result_str + "00"

        return result_str


