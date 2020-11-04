import unittest 
from Binary_search_tree import Binary_search_tree
from Node import Node

class testBinaryTree(unittest.TestCase):
    def setUp(self):
        self.binary_st = Binary_search_tree()

    def test_initiallEmptyTree_positive(self):
        self.assertIsNone(self.binary_st.print_tree())

    def test_insertOneValueToTreeAndCheckPresent_positive(self):
        tree = Binary_search_tree()
        tree.insert_value(2)
        self.assertTrue(tree.search(2))
    
    def test_insertOneValueToTreeAndCheckPresent_negative(self):
        tree = Binary_search_tree()
        tree.insert_value(5)
        self.assertFalse(tree.search(2))
    
    def test_insertHeightForOneElemenetInTree_positive(self):
        tree = Binary_search_tree()
        tree.insert_value(2)
        self.assertEqual(tree.height(), 1)
    
    def test_insertHeightForOneElemenetInTree_negative(self):
        tree = Binary_search_tree()
        tree.insert_value(2)
        self.assertNotEqual(tree.height(), 0)
    
    def test_insertFewValueToTreeAndCheckPresent_positive(self):
        tree = Binary_search_tree()
        tree.insert_value(2)
        tree.insert_value(3)
        tree.insert_value(5)
        self.assertTrue(tree.search(2) and tree.search(3) and tree.search(5))
    
    def test_insertFewValueToTreeAndCheckPresent_negative(self):
        tree = Binary_search_tree()
        tree.insert_value(2)
        tree.insert_value(3)
        tree.insert_value(10)
        tree.insert_value(45)
        self.assertFalse(tree.search(2) and tree.search(3) and tree.search(5))
    
    def test_addDublicatValueAndChekPresetInTree_positive(self):
        tree = Binary_search_tree()
        tree.insert_value(2)
        tree.insert_value(2)
        tree.insert_value(10)
        tree.insert_value(45)
        self.assertEqual(tree.height(), 3)
    
    def test_addDublicatValueAndChekPresetInTree_negative(self):
        tree = Binary_search_tree()
        tree.insert_value(2)
        tree.insert_value(2)
        tree.insert_value(10)
        tree.insert_value(45)
        self.assertNotEqual(tree.height(), 4)
    
    # def test_addValueAndChekPresetInTreeViaPrintFunction_positive(self):
    #     tree = Binary_search_tree()
    #     tree.insert_value(2)
    #     tree.insert_value(10)
    #     tree.insert_value(45)
    #     # tree.print_tree()
    #     self.assertIsNotNone(tree.print_tree())
    

if __name__ == '__main__':
    unittest.main()