def longest_word(sentence):
    # Remove punctuation that is likely to effect word length... 
    sentence = sentence.replace(".", "").replace("'","").replace("?", "").replace("!","")
    return_word = ""
    # Go through words in sentence, and store longest in return_word
    for word in sentence.split():
        if len(word) > len(return_word):
            return_word = word
    return return_word, len(return_word)
        
        
        
# With no easy base case (len = inf), we need to store inf as a len, and update return_word_lenth as we find shorter words
def shortest_word(sentence):
    # Remove punctuation that is likely to effect word length... 
    sentence = sentence.replace(".", "").replace("'","").replace("?", "").replace("!","")
    return_word = ""
    return_word_len = float("inf")
    
    # Go through words in sentence, and store shortest in return_word
    for word in sentence.split():
        if len(word) < return_word_len:
            return_word, return_word_len = word, len(word)
    return return_word.lower(), len(return_word)
    
    
import unittest

class Test(unittest.TestCase):
    
    def test(self):
        self.assertEqual(shortest_word("The cow jumped over the moon."), ('the', 3))
        self.assertEqual(shortest_word("He does not enquire into the abstract right and wrong of any case, but subjects it to the acid test of proletarian interests."), ('he', 2))
        self.assertEqual(shortest_word("Let's test a long sentence where the last word has a double ellipsis......"), ('a', 1))
        
        self.assertEqual(longest_word("The cow jumped over the moon."), ('jumped', 6))
        self.assertEqual(longest_word("He does not enquire into the abstract right and wrong of any case, but subjects it to the acid test of proletarian interests."), ('proletarian', 11))
        self.assertEqual(longest_word("Let's test a long sentence where the last word has a double ellipsis......"), ('sentence', 8))
        
   if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)