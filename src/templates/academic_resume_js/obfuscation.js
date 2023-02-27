//http://www.grall.name/posts/1/antiSpam-emailAddressObfuscation.html
function decode(a) {
    // ROT13 : a Caesar cipher 
    // letter -> letter' such that code(letter') = (code(letter) + 13) modulo 26
    return a.replace(/./g, function (c) {
        return String.fromCharCode(c.charCodeAt(0) + 13);
    })
};

function encode(a) {
    // ROT13 : a Caesar cipher 
    // letter -> letter' such that code(letter') = (code(letter) + 13) modulo 26
    return a.replace(/./g, function (c) {
        return String.fromCharCode(c.charCodeAt(0) - 13);
    })
};