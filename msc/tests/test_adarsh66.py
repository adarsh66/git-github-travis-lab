from nose.tools import assert_equal
from msc.rot13 import rot13

from msc.rot13 import rot13_char

def test_rot13_char():
	assert_equal("a", rot13_char("n"))

