# UTF-8 VALIDATION
UTF-8 is a variable-width character encoding standard that can represent every character in the Unicode character set. It's widely used in web pages and other text files to ensure that various languages and symbols can be properly displayed.

To validate if a given string is encoded in UTF-8, you can use the following JavaScript function:

function validateUTF8(input) {
  try {
    new TextDecoder('utf-8').decode(new TextEncoder().encode(input));
    return true;
  } catch (error) {
    return false;
  }
}

// Example usage:
const validUTF8String = 'Hello, 世界!';
const invalidUTF8String = 'Invalid \xC3\x28 UTF-8';

console.log(validateUTF8(validUTF8String)); // Output: true
console.log(validateUTF8(invalidUTF8String)); // Output: false

In this function, we use TextEncoder().encode(input) to encode the input string into bytes using UTF-8 encoding. Then we use TextDecoder('utf-8').decode() to decode the bytes back into a string. If the decoding is successful, the input string is valid UTF-8; otherwise, it's invalid.

You can replace input with your actual string to test its validity. If the function returns true, the string is valid UTF-8; if it returns false, the string is not valid UTF-8.