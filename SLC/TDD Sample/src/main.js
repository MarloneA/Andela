'use strict';

module.exports = {

    /* Find the factorial of an integer */
    computeFactorial: (value) => {
        //For non-numeric or negative input
        if (typeof(value) != 'number' || value < 0){
             return 'undefined';
        }
        //For normal input
        else {
            let factorial = 1;
            for (let counter = value; counter >=1; counter--){
                factorial = factorial * counter;
            }
            return factorial;
        }
    }

}