const brain = require('brain.js')

const network = new brain.NeuralNetwork()
// 1 the weakest but then it wins over 5 and 5 wins over 6
network.train([
    { input: [1,2], output: [1] }, // team 2 wins
    { input: [1,3], output: [1] }, // team 3 wins
    { input: [2,3], output: [0] }, // team 2 wins
    { input: [2,4], output: [1] }, // team 4 wins
])
console.log(network.run([1,4]));
console.log(network.run([4,1]));
console.log(network.run([2,1]));
