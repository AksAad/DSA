class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def signature(x):
            return ''.join(sorted(str(x)))
        power_signature = {signature(1 << i) for i in range(31)}
        return signature(n) in power_signature