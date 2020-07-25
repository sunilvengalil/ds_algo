import unittest

from sorting.linear import sort_string_of_lower_case_alphabet
from sorting.o_n2 import insert_into_sorted_list
from sorting.o_n2 import sort_string_of_lower_case_alphabet as insertion_sort


class CountingSort(unittest.TestCase):
    def test_counting_sort(self):

        string = "sunil"
        sorted_string = sort_string_of_lower_case_alphabet(string)
        self.assertEqual("".join(sorted(string)), sorted_string)
        sorted_insertion_sort = insertion_sort(string)
        print(sorted_string)
        self.assertEqual("".join(sorted(string)),sorted_insertion_sort)



    # def test_insert_into_sorted_list(self):
    #     inserted = insert_into_sorted_list("acejt",'g')
    #     self.assertEqual("acegjt", inserted)
    #     inserted = insert_into_sorted_list("bcegjt",'a')
    #     self.assertEqual("abcegjt", inserted)


if __name__ == '__main__':
    unittest.main()
