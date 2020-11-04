# Создать структуру данных типа дерево. 
# Каждый узел дерева должен иметь строковое представление в виде "путь к вершине". 
# Имплементировать методы который позволяют:
# - обходить дерево горизонтально и вертикально
# - добавлять элементы в дерево
# - делать вставку узла дерева.
# - выполнять поиск по атрибуту узла дерева
from Binary_search_tree import Binary_search_tree

class entryPoint:

    def fill_tree (tree, numElems = 10, max_int = 100):
        from random import randint
        for _ in range(numElems):
            currentEl = randint(0, max_int)
            tree.insert_value(currentEl)
        return tree

    if __name__ == '__main__':
        tree = Binary_search_tree()
        tree = fill_tree(tree)
        print("<---- old tree ---->")
        tree.print_tree()
        print("the hight : %s" % tree.height())
        print("<---- new tree ---->")
        tree.insert_value(1)
        tree.insert_value(3)
        tree.insert_value(12)
        tree.insert_value(56)
        tree.print_tree()
        print("the hight : %s" % tree.height())
        print("find element {a} in tree : {b}".format(a = 12, b = tree.find(12)))