const strA1 = "ABC";
const strB1 = "abc";
const expected1 = true;

const strA2 = "ABC";
const strB2 = "abd";
const expected2 = false;

const strA3 = "ABC";
const strB3 = "bc";
const expected3 = false;

/**
 * Determines whether or not the strings are equal, ignoring case.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} strA
 * @param {string} strB
 * @returns {boolean} If the strings are equal or not.
 */
const strA1 = "ABC";
const strB1 = "abc";

const strA2 = "ABC";
const strB2 = "abd";

const strA3 = "ABC";
const strB3 = "bc";

function caseInsensitiveStringCompare(strA, strB) {
    if (strA.toLocaleLowerCase() != strB.toLocaleLowerCase()) {
        return false;
    } else {
        return true;
    }

}
console.log(caseInsensitiveStringCompare(strA1, strB1))
console.log(caseInsensitiveStringCompare(strA2, strB2))
console.log(caseInsensitiveStringCompare(strA3, strB3))

const str1 = "object oriented programming";
const expected1 = "OOP";

// The 4 pillars of OOP
const str2 = "abstraction polymorphism inheritance encapsulation";
const expected2 = "APIE";

const str3 = "software development life cycle";
const expected3 = "SDLC";

// Bonus: ignore extra spaces
const str4 = "  global   information tracker    ";
const expected4 = "GIT";

/**
 * Turns the given str into an acronym.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string to be turned into an acronym.
 * @returns {string} The acronym.
 */
str1 = "object oriented programming";
str2 = "abstraction polymorphism inheritance encapsulation";
str3 = "software development life cycle";
str4 = "  global   information tracker    ";
const expected4 = "GIT";

function acronymize(str) {
    strArr = ste.trim(" ");
    console.log(strArr)
    var result = "";
    for (var i = 0; i < strArr.length; i++) {
        result += strArr[i][0].toUpperCase();

    }
    return result;
}
console.log(acronymize(str1))
console.log(acronymize(str2))
console.log(acronymize(str3))
console.log(acronymize(str4))

acronymize("abstraction polymorphism inheritance encapsulation")


// ===============
// Reverse String
// ===============

/* 
  String: Reverse
  Given a string,
  return a new string that is the given string reversed
*/

const str1 = "creature";
const expected1 = "erutaerc";

const str2 = "dog";
const expected2 = "god";

const str3 = "hello";
const expected3 = "olleh";

const str4 = "";
const expected4 = "";

// step1 string to become an array
// step2 to have it reverse
// step3 prepare for empty string

function reversestring(str){
    let reverseStr = '';
    for(var i=str.length-1; i >= 0; i--){
        reverseStr+=str[i];
    }
return reverseStr;
}
console.log(reverseString("creature"));
console.log(reverseString("dog"));
console.log(reverseString("hello"));
console.log(reverseString(""));

function reverseString(str) {
    return str.split("").reverse().join("");
}
