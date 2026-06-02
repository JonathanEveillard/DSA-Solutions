func isAnagram(s string, t string) bool {
	
	// Edge case if the strings do not match
	if len(s) != len(t){
		return false
	}

	// Create one Singular hasmap 
	hash_s := make(map[rune]int)

	// Populate Hashmap
	for _, letter := range s{
		hash_s[letter]++
	}

	// Content comparison by substraction
	for _, letter := range t{
		hash_s[letter]--
		if hash_s[letter] < 0 {
			return false
		}
	}

	return true
}
