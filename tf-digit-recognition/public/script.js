const canvas = document.getElementById('canvas');
const context = canvas.getContext('2d');

const mouse = { x: 0, y: 0 };

canvas.width = 280;
canvas.height = 280;
context.lineWidth = 20;
context.lineCap = 'round';
context.strokeStyle = '#FFFFFF';
context.fillStyle = '#000000';
context.fillRect(0, 0, canvas.width, canvas.height);

canvas.addEventListener('mousemove', (e) => {
    const rect = canvas.getBoundingClientRect();
    mouse.x = e.clientX - rect.left;
    mouse.y = e.clientY - rect.top;
});

const onPaint = () => {
    context.lineTo(mouse.x, mouse.y);
    context.stroke();
};

canvas.addEventListener('mousedown', () => {
    context.beginPath();
    context.moveTo(mouse.x, mouse.y);
    canvas.addEventListener('mousemove', onPaint);
});

canvas.addEventListener('mouseup', () => {
    canvas.removeEventListener('mousemove', onPaint);

    const smallCanvas = document.createElement('canvas');
    smallCanvas.width = 28;
    smallCanvas.height = 28;
    const smallCtx = smallCanvas.getContext('2d');
    smallCtx.drawImage(canvas, 0, 0, 28, 28);
    const imageData = smallCtx.getImageData(0, 0, 28, 28).data;

    const input = [];
    for (let i = 0; i < imageData.length; i += 4) {
        input.push(imageData[i] / 255);
    }

    predict(input);
});

document.getElementById('clear').addEventListener('click', () => {
    context.fillRect(0, 0, canvas.width, canvas.height);
    document.getElementById('number').textContent = '';
});

let model = null;

tf.loadGraphModel('model/model.json')
    .then((loadedModel) => {
        model = loadedModel;
    })
    .catch((err) => {
        console.error('err:', err);
    });

const predict = (input) => {
    if (model) {
        const tensor = tf.tensor(input).reshape([1, 28, 28, 1]);
        model.predict(tensor)
            .array()
            .then((scores) => {
                const predicted = scores[0].indexOf(Math.max(...scores[0]));
                document.getElementById('number').textContent = predicted;
            });
    } else {
        setTimeout(() => predict(input), 100);
    }
};
