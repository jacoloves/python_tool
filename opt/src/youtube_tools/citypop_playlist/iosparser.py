#! /usr/bin/env python

class iosPraser:

    def iso_parser(target_str):
        target_str = target_str.replace('PT', '')
        target_str = target_str.replace('H', ':')
        target_str = target_str.replace('M', ':')
        result_str = target_str.replace('S', '')

        return result_str


