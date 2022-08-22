class Jar:
    def __init__(self, capacity=12):
        if capacity<0:
            raise ValueError
        else:
            self.capacity=capacity
        self.size=0

    def __str__(self):
        str=""
        for i in range(self.size):
            str+="🍪"
        return str

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError
        else:
            self.size+=n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError
        else:
            self.size-=n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self,cap):
        self._capacity=cap

    @property
    def sizee(self) :
        return self._size

    @sizee.setter
    def size(self,size):
        self._size=size
