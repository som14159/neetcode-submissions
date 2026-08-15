class Solution {
   public:
    int findBestLetter(int arr[]) {
        int maxC = arr[0], result = 0;
        for (int i = 1; i < 26; i++) {
            if (arr[i] > maxC) {
                maxC = arr[i];
                result = i;
            }
        }
        return result;
    }
    int characterReplacement(string s, int k) {
        int start = 0, end = 0;
        char highestOccurenceLetter = s[0];
        int maxCount = 1, result = 1, replacements = 0;
        int arr[26] = {0};
        arr[highestOccurenceLetter - 'A'] = 1;
        for (int i = 1; i < s.size(); i++) {
            int index = s[i] - 'A';
            arr[index]++;
            end++;
            int bestLetter = findBestLetter(arr);
            int windowSize = end - start + 1;
            replacements = windowSize - arr[bestLetter];
            if (replacements > k) {
                while (start != end) {
                    int startIndex = s[start] - 'A';
                    arr[startIndex]--;
                    start++;
                    bestLetter = findBestLetter(arr);
                    windowSize--;
                    replacements = windowSize - arr[bestLetter];
                    if (replacements <= k) break;
                }
            }
            result = max(result, windowSize);
        }
        return result;
    }
};
