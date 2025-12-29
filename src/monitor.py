class StreamMonitor:
    """
    An implementation of the Boyer-Moore voting algorithm for 
    real-time majority detection in data streams.
    """
    def __init__(self, strict=True):
        self.candidate = None
        self.votes = 0
        self.strict = strict
        
    def process_element(self, element):
        """Finds a candidate for majority using O(1) space."""
        if self.votes == 0:
            self.candidate = element
            self.votes = 1
        elif element == self.candidate:
            self.votes += 1
        else:
            self.votes -= 1
        return self.candidate
    
    def verify_majority(self, data_stream):
        """
        Verifies if the candidate actually meets the threshold.
        Returns the candidate if successful, otherwise -1.
        """
        if not data_stream:
            return -1
            
        count = sum(1 for x in data_stream if x == self.candidate)
        n = len(data_stream)
        
        # Logic for Strict (> N/2) vs Weak (>= N/2)
        threshold = n / 2
        if self.strict:
            return self.candidate if count > threshold else -1
        return self.candidate if count >= threshold else -1