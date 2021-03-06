def cmp_words(a, b):
    if a[1] != b[1]:
        return b[1] - a[1]
    return cmp(a[0], b[0])

class HashHeap:

    def __init__(self):
        self.heap = [0]
        self.hash = {}

    def add(self, key, value):
        self.heap.append((key, value))
        self.hash[key] = self.heap[0] + 1
        self.heap[0] += 1
        self._siftup(self.heap[0])

    def remove(self, key):
        index = self.hash[key]
        self._swap(index, self.heap[0])
        del self.hash[self.heap[self.heap[0]][0]]
        self.heap.pop()
        self.heap[0] -= 1
        if index <= self.heap[0]:
            index = self._siftup(index)
            self._siftdown(index)

    def hasKey(self, key):
        return key in self.hash

    def min(self):
        return 0 if self.heap[0] == 0 else self.heap[1][1]

    def _swap(self, a, b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]
        self.hash[self.heap[a][0]] = a
        self.hash[self.heap[b][0]] = b

    def _siftup(self, index):
        while index != 1:
            if cmp_words(self.heap[index], self.heap[index / 2]) < 0:
                break
            self._swap(index, index / 2)
            index = index / 2
        return index

    def _siftdown(self, index):
        size = self.heap[0]
        while index < size:
            t = index
            if index * 2 <= size and cmp_words(self.heap[t], self.heap[index * 2]) < 0:
                t = index * 2
            if index * 2 + 1 <= size and cmp_words(self.heap[t], self.heap[index * 2 + 1]) < 0:
                t = index * 2 + 1
            if t == index:
                break
            self._swap(index, t)
            index = t
        return index

    def size(self):
        return self.heap[0]

    def pop(self):
        key, value = self.heap[1]
        self.remove(key)
        return value


class TopK:

    def __init__(self, k):
        self.k = k
        self.top_k = HashHeap()
        self.counts = {}

    def add(self, word):
        if word not in self.counts:
            self.counts[word] = 1
        else:
            self.counts[word] += 1

        if self.top_k.hasKey(word):
            self.top_k.remove(word)

        self.top_k.add(word, self.counts[word])

        if self.top_k.size() > self.k:
            self.top_k.pop()
    def topk(self):
        # Write your code here
        topk = self.top_k.heap[1:]
        topk.sort(cmp=cmp_words)
        return [ele[0] for ele in topk]