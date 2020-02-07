from __future__ import absolute_import
from __future__ import unicode_literals

from enum import Enum


class CreditCardOperationEnum(Enum):
    AuthOnly = 1,
    AuthAndCapture = 2,
    AuthAndCaptureWithDelay = 3
