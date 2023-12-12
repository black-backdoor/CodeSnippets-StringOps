function levenshteinDistance(word1, word2) {
    const lenWord1 = word1.length + 1;
    const lenWord2 = word2.length + 1;

    const matrix = Array.from({ length: lenWord1 }, () => Array(lenWord2).fill(0));

    for (let i = 0; i < lenWord1; i++) {
        matrix[i][0] = i;
    }

    for (let j = 0; j < lenWord2; j++) {
        matrix[0][j] = j;
    }

    for (let i = 1; i < lenWord1; i++) {
        for (let j = 1; j < lenWord2; j++) {
            const cost = word1[i - 1] === word2[j - 1] ? 0 : 1;
            matrix[i][j] = Math.min(
                matrix[i - 1][j] + 1,
                matrix[i][j - 1] + 1,
                matrix[i - 1][j - 1] + cost
            );
        }
    }

    return matrix[lenWord1 - 1][lenWord2 - 1];
}

function findClosestMatch(inputWord, wordList) {
    let closestWord = null;
    let minDistance = Infinity;

    for (const word of wordList) {
        const distance = levenshteinDistance(inputWord, word);
        if (distance < minDistance) {
            minDistance = distance;
            closestWord = word;
        }
    }

    return closestWord;
}

// Example usage
const inputWord = "kittn";
const wordList = ["kitten"];

const closestMatch = findClosestMatch(inputWord, wordList);
console.log(`The closest match to '${inputWord}' in the list is '${closestMatch}'`);
