class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # balloon
        rec = {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}
        mp = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        for s in text:
            if s in mp: mp[s] += 1
        
        return min(mp[s]//rec[s] for s in mp)


        
text = "krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"
Solution().maxNumberOfBalloons(text)