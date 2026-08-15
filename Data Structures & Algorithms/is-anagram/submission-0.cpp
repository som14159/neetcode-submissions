class Solution {
   public:
    bool isAnagram(string s, string t) {
        int arr1[26] = {0}, arr2[26] = {0};
        for (auto ch : s) {
            arr1[ch - 'a']++;
        }
        for (auto ch : t) {
            arr2[ch - 'a']++;
        }
        for (int i = 0; i < 26; i++) {
            if (arr1[i] != arr2[i]) return false;
        }
        return true;
    }
};
