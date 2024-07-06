class Range:
    def __init__(self, start, stop = None, step = 1):
        if step == 0:
            raise ValueError("step cannot be zero")

        if stop is None:
            start, stop = 0, start

        self._length = max(0, (stop - start + step - 1) // step)
        self._start = start
        self._step = step
        self._stop = stop

    def __len__(self):
        return self._length

    def __getitem__(self, k):
        if k < 0:
            # so if length is 50, and k = -1, it results in 49, which is the last item because python is 0 indexed
            k += len(self)

        if not (0 <= k < self._length):
            raise IndexError("index out of range")
        
        return self._start + k * self._step
    

        

