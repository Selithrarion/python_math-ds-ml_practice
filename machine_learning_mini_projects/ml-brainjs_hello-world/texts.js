const data = [
    {
        "text": "my unit test failed",
        "category": "software",
    },
    {
        "text": "tried the program but it was buggy",
        "category": "software",
    },
    {
        "text": "unit-tests",
        "category": "software",
    },
    {
        "text": "my unit test failed",
        "category": "software",
    },
    {
        "text": "code",
        "category": "software",
    },
    {
        "text": "bug",
        "category": "software",
    },

    {
        "text": "my new power supply",
        "category": "hardware",
    },
    {
        "text": "i need more RAM",
        "category": "hardware",
    },
    {
        "text": "my ssd is broken",
        "category": "hardware",
    },
    {
        "text": "i have 2tb ssd",
        "category": "hardware",
    },
]

const brain = require('brain.js')
const network = new brain.recurrent.LSTM()
const trainingData = data.map((i) => ({
    input: i.text,
    output: i.category
}))
network.train(trainingData, {
    iterations: 2000
})

console.log(network.run('i fixed the power supply'));
console.log(network.run('so many bugs'));
console.log(network.run('man u need to write unit tests here'));
console.log(network.run('i bought new ssd'));