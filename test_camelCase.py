from unittest import TestCase
import camelCase


class TestCamelCase(TestCase):

    def test_camelcase_sentence(self):
        self.assertEqual("helloWorld", camelCase.camel_case("Hello World"))
    
    def test_camelcase_blank_sentence(self):
        self.assertEqual("", camelCase.camel_case(""))
    
    def test_camelcase_emoji(self):
        self.assertEqual("💘🥀🗺🛫🎄💑", camelCase.camel_case("💘 🥀🗺🛫 🎄💑"))
    
    def test_camelcase_more_than_one_white_space(self):
        self.assertEqual("helloWorld", camelCase.camel_case("  Hello    World    "))
