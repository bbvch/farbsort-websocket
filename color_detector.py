import datetime


class ColorDetector(object):
  _STATE_IDLE = 1
  _STATE_DESCEND = 2
  _STATE_ASCEND = 3
  _LIMIT_TOLERANCE = 30
  _NO_OBJECT_LIMIT = 1225
  _BLUE_OBJECT_LIMIT = 1199 + _LIMIT_TOLERANCE
  _RED_OBJECT_LIMIT = 908 + _LIMIT_TOLERANCE
  _WHITE_OBJECT_LIMIT = 854 + _LIMIT_TOLERANCE

  def __init__(self, hal, verbose=False):
    self._hal = hal
    self._verbose = verbose
    self._last_adc_value = None
    self._state = None
    self._last_state = None

  def poll(self):
    adc_value = self.raw_value()
    if self._last_adc_value is not None:
      self.eval_state(adc_value)
      self.eval_object_color(adc_value)
      self._last_state = self._state
    self._last_adc_value = adc_value

  def eval_state(self, adc_value):
    if adc_value >= self._NO_OBJECT_LIMIT:
      if self._state != self._STATE_IDLE:
        print "state=idle"
      self._state = self._STATE_IDLE
    elif adc_value < self._last_adc_value:
      if self._state != self._STATE_DESCEND:
        print "state=descend"
      self._state = self._STATE_DESCEND
    elif adc_value > self._last_adc_value:
      if self._state != self._STATE_ASCEND:
        print "state=ascend"
      self._state = self._STATE_ASCEND

  def eval_object_color(self, adc_value):
      if ((self._state == self._STATE_ASCEND) and
          (self._last_state == self._STATE_DESCEND)):
        if self._last_adc_value < self._WHITE_OBJECT_LIMIT:
          print "Got WHITE object (value=%s)" % self._last_adc_value
        elif self._last_adc_value < self._RED_OBJECT_LIMIT:
          print "Got RED object (value=%s)" % self._last_adc_value
        elif self._last_adc_value < self._BLUE_OBJECT_LIMIT:
          print "Got BLUE object (value=%s)" % self._last_adc_value

  def raw_value(self):
    adc_value = self._hal.get_analog_input("AIN0")
    if self._verbose:
      if adc_value < self._NO_OBJECT_LIMIT:
        now = datetime.datetime.now()
        print "%s: AIN0=%u" % (now.isoformat(), adc_value)
    return adc_value
