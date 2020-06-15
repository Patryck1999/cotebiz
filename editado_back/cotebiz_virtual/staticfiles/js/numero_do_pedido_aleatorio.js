let output = document.getElementById('numero_do_pedido')
let output2 = document.getElementById('numero_de_leilao')

function getRandomNumber(min, max){
    let step1 = max - min + 1;
    let step2 = Math.random() * step1;
    let result = Math.floor(step2) + min;
    return result;

}
function createArrayOfNumbers(start, end){
    let myArray = [];

    for(let i = start; i<= end; i++){
        myArray.push(i);
    }

    return myArray;
}

let numbersArray = createArrayOfNumbers(100000,900000);

let randomIndex = getRandomNumber(0,numbersArray.length-1);
let randomNumber = numbersArray[randomIndex];
numbersArray.splice(randomIndex, 1);
output.value = randomNumber+70400;
output2.value = randomNumber+53000;