char findTheDifference(char *s, char *t) {
    int freq[26] = {0};

    while (*s != '\0') {
        freq[*s - 'a']++;
        s++;
    }


    while (*t != '\0') {
        if (freq[*t - 'a'] == 0 || --freq[*t - 'a'] < 0) {
            return *t;
        }
        t++;
    }

    return '\0'; 
}
