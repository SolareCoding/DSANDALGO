class BinSearch:
    def ascendingSolution(self, data, min_index, max_index, target):
        if max_index < min_index or min_index < 0:
            return -1
        if max_index == min_index:
            if target == data[max_index]:
                return max_index
            else:
                return -1
        mid_index = int((max_index + min_index) / 2)
        if data[mid_index] == target:
            return mid_index
        elif data[mid_index] > target:
            return self.ascendingSolution(data, min_index, mid_index-1, target)
        else:
            return self.ascendingSolution(data, mid_index+1, max_index, target)


if __name__ == "__main__":
    data = [1,2,3,4,5,6,7]
    bs = BinSearch()
    result = bs.ascendingSolution(data, 0, len(data)-1, 8)
    print('rearch result: ', result)