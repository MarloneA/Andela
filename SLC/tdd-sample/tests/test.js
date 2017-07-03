const assert = require('chai').assert;
const myApp = require('../src/main.js');

describe("Factorial", function(){

    describe("Handle valid input", function(){
        it("Should return 6 as factorial for 3", function(){
            assert.equal(myApp.computeFactorial(3), 6);
        }
        );
    }
    );

    describe("Handle invalid input", function(){
        it("Should return undefined as factorial for -5", function(){
            assert.equal(myApp.computeFactorial(-5), 'undefined');
        }
        );
    }
    );
}

);