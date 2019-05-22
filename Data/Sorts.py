class Sorts:
    def __init__(self):
        self.list01 = [3, 4, 1, 5, 2, 9, 6, 8, 7, 5]

    def bubble_sort(self):
        for item in range(len(self.list01)-1):
            for c in range(len(self.list01) - item-1):
                if self.list01[c] > self.list01[c+1]:
                    self.list01[c], self.list01[c+1] = self.list01[c+1], self.list01[c]

        print(self.list01)

    def select_sort(self):
        for item in range(len(self.list01)-1):
            mini = self.list01[item]
            for c in range(item+1, len(self.list01)):
                if self.list01[c] < mini:
                    mini = self.list01[c]
                if self.list01[item] != mini:
                    self.list01[c] = self.list01[item]
                    self.list01[item] = mini
        print(self.list01)

    def insert_sort(self):
        for item in range(1, len(self.list01)):
            x = self.list01[item]
            j = item
            while j > 0 and self.list01[j-1] > x:
                self.list01[j] = self.list01[j-1]
                j -= 1
            self.list01[j] = x
        print(self.list01)

    def sub_sort(self, low, high):
        key = self.list01[low]
        while low < high:
            while low < high and self. list01[high] >= key:
                high -= 1
            self.list01[low] = self.list01[high]
            while low < high and self.list01[low] < key:
                low += 1
            self.list01[high] = self.list01[low]
        self.list01[low] = key
        return low

    def quick(self, low, high):
        if low < high:
            key = self.sub_sort(low, high)
            self.quick(low, key - 1)
            self.quick(key+1, high)

if __name__ == "__main__":
    i = Sorts()
    # i.bubble_sort()
    # i.select_sort()
    # i.insert_sort()
    i.quick(0, len(i.list01)-1)
    print(i. list01)