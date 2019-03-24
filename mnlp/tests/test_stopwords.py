from unittest import TestCase

import mnlp


class TestStopwords(TestCase):

    def test_is_list(self):
        s = mnlp.stopwords.words()
        self.assertTrue(isinstance(s, list))
