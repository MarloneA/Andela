import pytest
from binary_search import List
from binary_search import BinarySearch

""" Test List Creation """

def test_list_creation_one(): # normal list creation
    new_list = List(4, 2)
    assert new_list.create_list() == [2, 4, 6, 8]
    assert new_list.length == 4

def test_list_creation_two(): # normal list creation with a different size and step
    new_list = List(9, 1)
    assert new_list.create_list() == [2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert new_list.length == 9

def test_list_creation_empty(): # creation of an empty list
    new_list = List(0, 5)
    assert new_list.create_list() == []
    assert new_list.length == 0

def test_list_creation_one_element(): # create a single element list
    new_list = List(1, 3)
    assert new_list.create_list() == [2]
    assert new_list.length == 1

def test_list_creation_no_step(): # list with no step -> same elements
    new_list = List(3, 0)
    assert new_list.create_list() == [2, 2, 2]
    assert new_list.length == 3

def test_list_creation_no_length_no_step(): # list with no element and no step -> empty list
    new_list = List(0, 0)
    assert new_list.create_list() == []
    assert new_list.length == 0
    
""" Test Binary Search """

def test_binary_search_small_list(): # test small list
    new_search = BinarySearch(3, 1)
    assert new_search.search(3) == {'work_done': 1}

def test_binary_search_medium_list(): # test medium list
    new_search = BinarySearch(5, 2)
    assert new_search.search(8) == {'work_done': 2}

def test_binary_search_medium_list(): # test large list
    new_search = BinarySearch(10, 3)
    assert new_search.search(5) == {'work_done': 2}