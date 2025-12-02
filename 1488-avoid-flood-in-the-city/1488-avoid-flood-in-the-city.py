class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        st = SortedSet()
        full_lakes = {}
        answer = [1 for i in range(len(rains))]

        for i, lake in enumerate(rains):
            if lake == 0:
                st.add(i)
            else:
                if lake in full_lakes:
                    index = full_lakes[lake]
                    it = st.bisect_left(index)
                    if it == len(st):
                        return []
                    answer[st[it]] = lake
                    st.pop(it) 
                    
                answer[i] = -1
                full_lakes[lake] = i
        return answer
                