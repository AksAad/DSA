class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        count = {}
        for i in range(0,len(languages)):
            count[i+1] = set(languages[i])
        problematic_users = set()

        for u, v in friendships:
            if not (count[u] & count[v]):
                problematic_users.add(u)
                problematic_users.add(v)

        lang_count = defaultdict(int)
        for user in problematic_users:
            for lang in count[user]:
                lang_count[lang] += 1

        best = max(lang_count.values(), default=0)
        return len(problematic_users) - best

        