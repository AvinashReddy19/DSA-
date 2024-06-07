class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # Sort the dictionary by length to ensure the shortest root is tried first
        dictionary.sort(key=len)
        sent = sentence.split(' ')
        
        for idx, word in enumerate(sent):
            for root in dictionary:
                if word.startswith(root):
                    sent[idx] = root
                    break
        
        return ' '.join(sent)