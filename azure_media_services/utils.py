# -*- coding: utf-8 -*-
"""
Copyright (c) Microsoft Corporation. All Rights Reserved.

Licensed under the MIT license. See LICENSE file on the project webpage for details.
"""


def _(text):
    """
    Make '_' a no-op so we can scrape strings.
    """
    return text
