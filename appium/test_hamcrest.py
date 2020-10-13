from hamcrest import *

class TestApp:
    def test_hamcrest(self):
        # assert_that(10,equal_to(9),'这是一个提示')
        assert_that(8,close_to(10,2))
        assert_that("contains some string",contains_string("string"))
