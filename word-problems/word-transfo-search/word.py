class Node:
    def __init__(self, val=None):
        self.val = val
        self.nexts = {}
        self.leaf = False


class Trie:
    def __init__(self, words=[]):
        self.root = Node()
        for word in words:
            self.insert(word)

    def insert(self, word):
        node = self.root
        for i, ch in enumerate(word):
            if node.nexts.get(ch) is None:
                node.nexts[ch] = Node(ch)
            node = node.nexts[ch]
        node.leaf = True

    def search(self, word):
        node = self.root
        for i, ch in enumerate(word):
            if node.nexts.get(ch) is None:
                return False
            node = node.nexts[ch]
        if not node.leaf:
            return False
        return True

    def search_all_sub_words(self, word):
        sub_words = set()
        build_word = ""
        node = self.root
        for i, ch in enumerate(word):
            if node.nexts.get(ch) is None:
                return False
            node = node.nexts[ch]
            build_word += ch
            if node.leaf:
                sub_words.add(build_word)
        return sub_words


class WordTransformationSearch:
    def __init__(self):
        self.trie = None

    def _gen_trie(self, words):
        self.trie = Trie(words)

    def find(self, words, grid):
        self._gen_trie(words)
        solution = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                solution += self.dfs(i, j, grid)

        return solution

    def dfs(self, i, j, grid):
        solutions = []
        directions = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0],
            [-1, -1],
            [-1, 1],
            [1, -1],
            [1, 1],
        ]
        for a, b in directions:
            di = i
            dj = j
            build = ""
            while di < len(grid) and dj < len(grid[0]) and di > -1 and dj > -1:
                build += grid[di][dj]
                di += a
                dj += b

            sub_words = self.trie.search_all_sub_words(build)
            if sub_words:
                for word in sub_words:
                    solutions.append([(i, j), word, (a, b)])

        return solutions


grid = [
    ["A", "B", "A", "C", "K", "Y"],
    ["A", "O", "E", "O", "P", "O"],
    ["D", "L", "N", "D", "A", "B"],
]

words = ["BACK", "BED", "BE", "PI", "BONE", "BACKY", "YOB", "BOY"]
wordsearch = WordTransformationSearch()
res = wordsearch.find(words, grid)
print(
    f"""
{res}
"""
    == f"""
{[
    [(0, 1), "BACK", (0, 1)],
    [(0, 1), "BACKY", (0, 1)],
    [(0, 1), "BED", (1, 1)],
    [(0, 1), "BE", (1, 1)],
    [(0, 5), "YOB", (1, 0)],
    [(2, 5), "BOY", (-1, 0)],
]}
"""
)
