import camelcase
from unittest import TestCase

class TestCamelCase(TestCase):

    def test_camelcase_sentence(self):

        self.assertEqual('helloWorld', camelcase.camel_case('Hello World'))

    def test_camelcase_blank_sentence(self):

        self.assertEqual('', camelcase.camel_case(''))

    def test_camelcase_strings_with_number(self):

        self.assertEqual('one1', camelcase.camel_case('One1'))
    
    def test_camelcase_stings_with_punctuation(self):

        self.assertEqual('hello.', camelcase.camel_case('Hello.')) 

    def test_camelcase_emoji(self):

        self.assertEqual('😂', camelcase.camel_case('😂'))

    def test_camelcase_newlines(self):
        
        self.assertEqual('hello\n', camelcase.camel_case('Hello\n'))

    def test_camelcase_whitespace_before(self):
        
        self.assertEqual('hello', camelcase.camel_case(' Hello'))

    def test_camelcase_whitespace_after(self):
        
        self.assertEqual('hello', camelcase.camel_case('Hello '))

    def test_camelcase_space_between_words(self):

        self.assertEqual('helloWorld', camelcase.camel_case('Hello            \tWorld      '))