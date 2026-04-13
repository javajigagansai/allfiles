const canvas = document.getElementById('heartCanvas');
const ctx = canvas.getContext('2d');

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const particles = [];
const particleCount = 600; // Increase for a denser heart
const heartPoints = [];
const colors = ['#ff4d6d', '#ff758f', '#c9184a', '#ffb3c1', '#ff0054'];

// Heart mathematical formula
function getHeartPoint(t) {
    const x = 16 * Math.pow(Math.sin(t), 3);
    const y = -(13 * Math.cos(t) - 5 * Math.cos(2 * t) - 2 * Math.cos(3 * t) - Math.cos(4 * t));
    return { x: x * 15, y: y * 15 }; // Scale by 15
}

// Pre-calculate points for the heart shape
for (let i = 0; i < particleCount; i++) {
    const t = Math.random() * Math.PI * 2;
    heartPoints.push(getHeartPoint(t));
}

class Particle {
    constructor(index) {
        this.index = index;
        this.reset();
    }

    reset() {
        this.x = Math.random() * canvas.width;
        this.y = Math.random() * canvas.height;
        this.size = Math.random() * 5 + 2;
        this.color = colors[Math.floor(Math.random() * colors.length)];
        this.target = heartPoints[this.index];
        this.speed = Math.random() * 0.02 + 0.01;
    }

    update() {
        // Move towards the heart target
        const tx = this.target.x + canvas.width / 2;
        const ty = this.target.y + canvas.height / 2;
        
        this.x += (tx - this.x) * this.speed;
        this.y += (ty - this.y) * this.speed;

        // Add a slight "floaty" wiggle
        this.x += Math.sin(Date.now() * 0.002 + this.index) * 0.5;
        this.y += Math.cos(Date.now() * 0.002 + this.index) * 0.5;
    }

    draw() {
        ctx.fillStyle = this.color;
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.fill();
    }
}

function init() {
    for (let i = 0; i < particleCount; i++) {
        particles.push(new Particle(i));
    }
}

function animate() {
    ctx.fillStyle = 'rgba(0, 0, 0, 0.1)'; // Creates a slight trail effect
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    particles.forEach(p => {
        p.update();
        p.draw();
    });

    requestAnimationFrame(animate);
}

window.addEventListener('resize', () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
});

init();
animate();