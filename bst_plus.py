from bst import BinarySearchTree


class BstPlus(BinarySearchTree):
    """
    this class is a binary search tree plus some additional functionality
    that you will implement.

    first take a look at bst.py to see the methods that are provided for you
    you will be implementing the following methods:
    - mirror
    - countLeaves
    - height
    - min
    - max
    - reversed 
    """

    def mirror(self) -> None:
        """Switch the left and right sides of every node."""
        def swap(node):
            if node is None:
                return

            left = node.left()
            node.set_left(node.right())
            node.set_right(left)

            swap(node.left())
            swap(node.right())

        swap(self._root)

    def countLeaves(self) -> int:
        """Count nodes that have no children."""
        def count(node):
            if node is None:
                return 0
            if node.left() is None and node.right() is None:
                return 1
            return count(node.left()) + count(node.right())

        return count(self._root)

    def height(self) -> int:
        """Count the levels along the longest path."""
        def levels(node):
            if node is None:
                return 0

            left = levels(node.left())
            right = levels(node.right())
            return 1 + max(left, right)

        return levels(self._root)

    def min(self) -> any:
        """Find the smallest value in the tree."""
        if self._root is None:
            raise ValueError('Tree is empty')

        node = self._root
        while node.left() is not None:
            node = node.left()
        return node.value()

    def max(self) -> any:
        """Find the largest value in the tree."""
        if self._root is None:
            raise ValueError('Tree is empty')

        node = self._root
        while node.right() is not None:
            node = node.right()
        return node.value()

    def reversed(self):
        """Visit the values from largest to smallest."""
        def visit(node):
            if node is None:
                return
            yield from visit(node.right())
            yield node.value()
            yield from visit(node.left())

        yield from visit(self._root)


#-----------------------------------

#    Helper functions for main()

#-----------------------------------

def check(name, actual, expected):
    """Print PASS or FAIL for a single test."""
    if actual == expected:
        print(f'PASS: {name}')
    else:
        print(f'FAIL: {name} -- expected {expected}, got {actual}')


def check_error(name, func):
    """Print PASS if func raises a ValueError, FAIL otherwise."""
    try:
        func()
        print(f'FAIL: {name} -- no error raised')
    except ValueError:
        print(f'PASS: {name}')


def build(values):
    tree = BstPlus()
    for v in values:
        tree.insert(v)
    return tree


#-----------------------------------

#          Test driver code

#-----------------------------------

def main():
    # Empty tree
    empty = BstPlus()
    # Single element tree
    single = build([5])
    # Balanced-ish tree with 4 leaves (10, 40, 60, 80) and 4 levels
    tree = build([50, 30, 70, 20, 40, 60, 80, 10])
    # Skewed tree: every node only has a right child
    skewed = build([1, 2, 3, 4, 5])

    print('--- empty tree ---')
    print('original tree:')
    print(empty)
    check('empty tree has 0 leaves', empty.countLeaves(), 0)
    check('empty tree has height 0', empty.height(), 0)
    check_error('min of empty tree throws error', empty.min)
    check_error('max of empty tree throws error', empty.max)
    check('empty tree reverse is empty', list(empty.reversed()), [])
    empty.mirror()
    print('mirrored tree:')
    print(empty)
    print()

    print('--- single node tree ---')
    print('original tree:')
    print(single)
    check('single node tree has 1 leaf', single.countLeaves(), 1)
    check('single node tree has height 1', single.height(), 1)
    check('min of single node tree is 5', single.min(), 5)
    check('max of single node tree is 5', single.max(), 5)
    check('single node reversed is itself', list(single.reversed()), list(single))
    single.mirror()
    print('mirrored tree:')
    print(single)
    print()

    print('--- regular tree ---')
    print('original tree:')
    print(tree)
    check('regular tree has 4 leaf', tree.countLeaves(), 4)
    check('regular tree has height 4', tree.height(), 4)
    check('min of regular tree is 10', tree.min(), 10)
    check('max of regular tree is 80', tree.max(), 80)
    check('regular tree reverses properly', list(tree.reversed()), [80, 70, 60, 50, 40, 30, 20, 10])
    tree.mirror()
    print('mirrored tree:')
    print(tree)
    print()

    print('--- skewed tree ---')
    print('original tree:')
    print(skewed)
    check('skewed tree has 1 leaf', skewed.countLeaves(), 1)
    check('skewed tree has height 5', skewed.height(), 5)
    check('min of skewed tree is 1', skewed.min(), 1)
    check('max of skewed tree is 5', skewed.max(), 5)
    check('skewed tree reverses properly', list(skewed.reversed()), [5, 4, 3, 2, 1])
    skewed.mirror()
    print('mirrored tree:')
    print(skewed)

if __name__ == '__main__':
    main()