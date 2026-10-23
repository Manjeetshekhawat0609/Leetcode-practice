
class Solution {
    public boolean arrayStringsAreEqual(String[] word1, String[] word2) {
        StringBuilder sb = new StringBuilder();
        StringBuilder sb1 = new StringBuilder();
        for (int i = 0; i < word1.length; i++) {
            for (int j = 0; j < word1[i].length(); j++) {
                sb.append(word1[i].charAt(j));
            }
        }
        for (int i = 0; i < word2.length; i++) {
            for (int j = 0; j < word2[i].length(); j++) {
                sb1.append(word2[i].charAt(j));
            }
        }
        return sb.toString().equals(sb1.toString());
    }
}
