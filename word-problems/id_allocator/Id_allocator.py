import heapq
REMOVED = "<removed>"
ALLOCATED = "<allocated>"

class Id_allocator:
    def __init__(self, capacity=500):
        self.capacity = capacity
        self.allocated_list = []
        self.allocated_i_dic = {}
        self.removed_heap = []
        self._initialize_priority_and_heaps()

    def _initialize_priority_and_heaps(self):
        tmp = [(i, REMOVED) for i in range(50,self.capacity)]
        # print('tmp', tmp)
        self.allocated_list = tmp[:]
        self.allocated_list.sort()

        self.removed_heap = tmp[:]
        heapq.heapify(self.removed_heap)
        for i, tup in enumerate(self.allocated_list):
            id_num, status = tup
            self.allocated_i_dic[id_num] = i

    def _get_allocated_id_tup(self, id_num):
        """
        Returns the allocated id tuple (id, status)
        Returns None if does not exist
        """
        i = self.allocated_i_dic.get(id_num, False)
        if not i:
            return None
        return self.allocated_list[i]

    def _set_allocated_id_tup(self, id_num, status):
        """
        Changes the status of the id_num in allocated heap
        """
        i = self.allocated_i_dic.get(id_num, None)
        if i is None:
            raise Exception("This id was not pre-allocated in the capacity of the heap.")
            
        self.allocated_heap[i] = (id_num, status)
        return self.allocated_list[i]

    def allocate(self):
        # Returns any un-allocated id
        if self.removed_heap:
            # print('poppoing min heap self.removed_heap', self.removed_heap.pop())
            available_id, status = heapq.heappop(self.removed_heap)
            return self._set_allocated_id_tup(available_id, ALLOCATED)
        else:
            raise Exception(f"Allocations are over the capacity allowed: {self.capacity}")

    def remove(self, id_num):
        # 1. Check if this id was already removed.
        id_val, status = self._get_allocated_id_tup(id_num)
        if status == REMOVED:
            raise Exception(f"Id {id_num} was already removed from the pool.")
        # 2. Change status and add to removed heap.
        if status == ALLOCATED:
            tup = (id_num, REMOVED)
            heapq.heappush(self.removed_heap, tup)
            self._set_allocated_id_tup(id_num, REMOVED)
            return True

    def allocate_specific(self, id):
        pass

idalloc = Id_allocator()
res = idalloc.allocate(); print(res)
res = idalloc.allocate(); print(res)
res = idalloc.allocate(); print(res)
res = idalloc.allocate(); print(res)
res = idalloc.remove(52); print(res)
print("allocated: -----")
print(idalloc.allocated_heap[0:10])
print("removed: -----")
print(idalloc.removed_heap[0:10])