class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        queue = []
        for i in nums:
            if str(i) in hash_map:
                hash_map[str(i)] +=1
            else:
                hash_map[str(i)] = 1
        print(hash_map)
        # for i in hash_map:
        #     if len(queue)<k:
        #         queue.append(i)
        #         queue = sorted(queue,key=lambda x: hash_map[x],reverse=True)
        #     else:
        #         if hash_map[queue[0]] < hash_map[i]:
        #             queue.pop(-1)
        #             queue.append(i)
        #             queue = sorted(queue,key=lambda x: hash_map[x],reverse = True)
        sorted_keys = sorted(hash_map.keys(),key= lambda x:hash_map[x],reverse = True)
        i=0
        while i<k:
            queue.append(int(sorted_keys[i]))
            i+=1


        return queue


        