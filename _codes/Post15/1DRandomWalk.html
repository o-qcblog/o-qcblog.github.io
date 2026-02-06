<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>1D Random Walk Visualization</title>
    <style>
        :root {
            --primary-color: #3b82f6; /* Blue */
            --coin-color: #f59e0b;    /* Amber/Gold */
            --bg-color: #f8fafc;      /* Slate 50 */
            --text-color: #334155;    /* Slate 700 */
            --line-color: #94a3b8;    /* Slate 400 */
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: transparent; /* Transparent for embedding */
            color: var(--text-color);
            margin: 0;
            padding: 20px;
            display: flex;
            justify-content: center;
        }

        .container {
            display: flex;
            flex-wrap: wrap;
            max-width: 900px;
            width: 100%;
            gap: 20px;
            background: white;
            border-radius: 12px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            padding: 20px;
            border: 1px solid #e2e8f0;
        }

        /* Left Column: Visualizations */
        .viz-column {
            flex: 2;
            min-width: 300px;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .canvas-wrapper {
            position: relative;
            width: 100%;
            height: 180px;
            background: #f1f5f9;
            border-radius: 8px;
            border: 1px solid #e2e8f0;
            overflow: hidden;
        }

        .canvas-label {
            position: absolute;
            top: 8px;
            left: 10px;
            font-size: 0.85rem;
            font-weight: 600;
            color: #64748b;
            background: rgba(255,255,255,0.8);
            padding: 2px 6px;
            border-radius: 4px;
        }

        canvas {
            display: block;
            width: 100%;
            height: 100%;
        }

        /* Right Column: Controls */
        .controls-column {
            flex: 1;
            min-width: 200px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-start;
            padding: 10px;
            background: #f8fafc;
            border-radius: 8px;
            border: 1px solid #e2e8f0;
        }

        /* Coin Styles */
        .coin-scene {
            width: 100px;
            height: 100px;
            perspective: 600px;
            margin-bottom: 20px;
            cursor: pointer;
        }

        .coin {
            width: 100%;
            height: 100%;
            position: relative;
            transform-style: preserve-3d;
            transition: transform 0.5s ease-out;
        }

        .coin.flipping {
            animation: flipAnimation 0.5s infinite linear;
        }

        @keyframes flipAnimation {
            0% { transform: rotateY(0deg); }
            100% { transform: rotateY(360deg); }
        }

        .coin-face {
            position: absolute;
            width: 100%;
            height: 100%;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2rem;
            font-weight: bold;
            color: white;
            backface-visibility: hidden;
            box-shadow: inset 0 0 10px rgba(0,0,0,0.3), 0 4px 6px rgba(0,0,0,0.2);
            border: 4px solid #fff;
        }

        .coin-front {
            background: var(--coin-color);
            transform: rotateY(0deg);
        }

        .coin-back {
            background: #cbd5e1; /* Silver/Gray for Tails */
            color: #475569;
            transform: rotateY(180deg);
        }

        .instruction {
            margin-top: -10px;
            margin-bottom: 20px;
            font-size: 0.8rem;
            color: #64748b;
        }

        /* Slider Styles */
        .slider-group {
            width: 100%;
            margin-bottom: 20px;
            text-align: center;
        }

        .slider-label {
            display: flex;
            justify-content: space-between;
            font-size: 0.8rem;
            margin-bottom: 5px;
            font-weight: 500;
        }

        input[type=range] {
            width: 100%;
            accent-color: var(--primary-color);
        }

        .bias-display {
            font-weight: bold;
            color: var(--primary-color);
        }

        /* Stats */
        .stats {
            width: 100%;
            text-align: left;
            font-size: 0.9rem;
            margin-bottom: 20px;
            padding: 10px;
            background: white;
            border-radius: 6px;
            border: 1px solid #e2e8f0;
        }

        .stat-row {
            display: flex;
            justify-content: space-between;
            margin-bottom: 4px;
        }

        .btn-reset {
            padding: 8px 16px;
            background-color: #ef4444;
            color: white;
            border: none;
            border-radius: 6px;
            font-weight: 600;
            cursor: pointer;
            transition: background 0.2s;
        }

        .btn-reset:hover {
            background-color: #dc2626;
        }

    </style>
</head>
<body>

<div class="container">
    <!-- Left Column: Visuals -->
    <div class="viz-column">
        <!-- Part 1: Random Walk -->
        <div class="canvas-wrapper">
            <div class="canvas-label">Random Walk</div>
            <canvas id="walkCanvas"></canvas>
        </div>
        
        <!-- Part 3: Probability Distribution -->
        <div class="canvas-wrapper">
            <div class="canvas-label">Probability Distribution</div>
            <canvas id="distCanvas"></canvas>
        </div>
    </div>

    <!-- Right Column: Controls -->
    <div class="controls-column">
        <!-- Part 2: Coin -->
        <h3>Click Coin</h3>
        <div class="coin-scene" id="coinBtn">
            <div class="coin" id="coin">
                <div class="coin-face coin-front">H</div>
                <div class="coin-face coin-back">T</div>
            </div>
        </div>
        <div class="instruction">Click to toss</div>

        <!-- Bias Slider -->
        <div class="slider-group">
            <div class="slider-label">
                <span>Tails</span>
                <span>Fair</span>
                <span>Heads</span>
            </div>
            <input type="range" id="biasSlider" min="0" max="1" step="0.05" value="0.5">
            <div style="margin-top: 5px; font-size: 0.9rem;">
                P(Heads) = <span id="biasValue" class="bias-display">0.50</span>
            </div>
        </div>

        <!-- Stats -->
        <div class="stats">
            <div class="stat-row">
                <span>Steps:</span>
                <span id="stepCount">0</span>
            </div>
            <div class="stat-row">
                <span>Position:</span>
                <span id="posCount">0</span>
            </div>
        </div>

        <button class="btn-reset" id="resetBtn">Reset</button>
    </div>
</div>

<script>
    // State
    const state = {
        position: 0,
        steps: 0,
        history: [0], // Array of positions
        bias: 0.5,
        probabilities: { 0: 1 }, // Map of position -> probability
        isFlipping: false,
        viewRange: 10, // +/- range to show on x-axis
        facing: 1 // 1 = right, -1 = left
    };

    // DOM Elements
    const walkCanvas = document.getElementById('walkCanvas');
    const distCanvas = document.getElementById('distCanvas');
    const coinBtn = document.getElementById('coinBtn');
    const coin = document.getElementById('coin');
    const biasSlider = document.getElementById('biasSlider');
    const biasValue = document.getElementById('biasValue');
    const stepCount = document.getElementById('stepCount');
    const posCount = document.getElementById('posCount');
    const resetBtn = document.getElementById('resetBtn');

    // Contexts
    const ctxWalk = walkCanvas.getContext('2d');
    const ctxDist = distCanvas.getContext('2d');

    // Initialization
    function init() {
        resizeCanvases();
        window.addEventListener('resize', () => {
            resizeCanvases();
            drawAll();
        });
        
        biasSlider.addEventListener('input', (e) => {
            state.bias = parseFloat(e.target.value);
            biasValue.textContent = state.bias.toFixed(2);
        });

        coinBtn.addEventListener('click', tossCoin);
        resetBtn.addEventListener('click', reset);

        drawAll();
    }

    function resizeCanvases() {
        // Handle HiDPI screens
        const dpr = window.devicePixelRatio || 1;
        const rect = walkCanvas.parentElement.getBoundingClientRect();
        
        [walkCanvas, distCanvas].forEach(canvas => {
            canvas.width = rect.width * dpr;
            canvas.height = rect.height * dpr;
            canvas.style.width = `${rect.width}px`;
            canvas.style.height = `${rect.height}px`;
            const ctx = canvas.getContext('2d');
            ctx.scale(dpr, dpr);
        });
    }

    function reset() {
        state.position = 0;
        state.steps = 0;
        state.history = [0];
        state.probabilities = { 0: 1 };
        state.viewRange = 10;
        state.facing = 1;
        
        stepCount.textContent = 0;
        posCount.textContent = 0;
        
        // Reset visual coin rotation
        coin.style.transform = 'rotateY(0deg)';
        
        drawAll();
    }

    // --- Logic ---

    function updateProbabilities() {
        const newProbs = {};
        const p = state.bias;
        const q = 1 - p;

        // Iterate over current existing positions in distribution
        // P(x, t) = P(x-1, t-1)*p + P(x+1, t-1)*q
        // But easier: Push forward.
        // If we are at pos X with prob P, next step we send P*p to X+1 and P*q to X-1.
        
        for (const [posStr, prob] of Object.entries(state.probabilities)) {
            const pos = parseInt(posStr);
            
            // Move Right (Heads)
            if (!newProbs[pos + 1]) newProbs[pos + 1] = 0;
            newProbs[pos + 1] += prob * p;

            // Move Left (Tails)
            if (!newProbs[pos - 1]) newProbs[pos - 1] = 0;
            newProbs[pos - 1] += prob * q;
        }
        state.probabilities = newProbs;
    }

    function tossCoin() {
        if (state.isFlipping) return;
        state.isFlipping = true;

        // Visual Flip Animation
        coin.classList.add('flipping');

        // Determine result immediately but show after delay
        const isHeads = Math.random() < state.bias;
        
        setTimeout(() => {
            coin.classList.remove('flipping');
            
            // Set final rotation based on result
            // If Heads, 0deg (or 360, 720). If Tails, 180deg.
            // We use a cumulative rotation to prevent spinning backward
            const currentRotation = coin.style.transform ? parseInt(coin.style.transform.replace(/[^\d]/g, '')) : 0;
            // Align to nearest full flip
            let base = Math.ceil(currentRotation / 360) * 360; 
            
            if (isHeads) {
                coin.style.transform = `rotateY(${base + 360}deg)`; // Land on Front
                state.position++;
                state.facing = 1;
            } else {
                coin.style.transform = `rotateY(${base + 180}deg)`; // Land on Back
                state.position--;
                state.facing = -1;
            }

            // Logic Updates
            state.steps++;
            state.history.push(state.position);
            updateProbabilities();

            // Stats Update
            stepCount.textContent = state.steps;
            posCount.textContent = state.position;

            // Auto-scale view
            if (Math.abs(state.position) > state.viewRange - 2) {
                state.viewRange += 5;
            }

            drawAll();
            state.isFlipping = false;

        }, 600); // 600ms flip duration
    }

    // --- Drawing ---

    function getX(pos, width) {
        // Map integer pos to canvas X
        // Center is 0
        const unit = width / (state.viewRange * 2 + 1);
        const center = width / 2;
        return center + (pos * unit);
    }

    function drawGrid(ctx, width, height, isDist = false) {
        ctx.clearRect(0, 0, width, height);
        
        const unit = width / (state.viewRange * 2 + 1);
        const center = width / 2;
        const axisY = isDist ? height - 30 : height / 2 + 30; // Shift axis depending on graph type

        // Main Axis Line
        ctx.beginPath();
        ctx.strokeStyle = '#94a3b8';
        ctx.lineWidth = 2;
        ctx.moveTo(10, axisY);
        ctx.lineTo(width - 10, axisY);
        ctx.stroke();

        // Ticks and Numbers
        ctx.textAlign = 'center';
        ctx.font = '12px sans-serif';
        ctx.fillStyle = '#64748b';

        for (let i = -state.viewRange; i <= state.viewRange; i++) {
            const x = getX(i, width);
            
            // Draw Ticks
            ctx.beginPath();
            ctx.moveTo(x, axisY - 5);
            ctx.lineTo(x, axisY + 5);
            ctx.stroke();

            // Draw Numbers (skip some if crowded)
            if (state.viewRange > 15 && i % 2 !== 0) continue;
            if (state.viewRange > 30 && i % 5 !== 0) continue;
            
            ctx.fillText(i, x, axisY + 20);
        }

        return { axisY, unit };
    }

    function drawStickFigure(ctx, x, y, facing) {
        ctx.strokeStyle = '#3b82f6'; // Blue
        ctx.fillStyle = '#3b82f6';
        ctx.lineWidth = 3;
        const scale = 0.8;

        // Head
        ctx.beginPath();
        ctx.arc(x, y - 50*scale, 10*scale, 0, Math.PI * 2);
        ctx.fill();

        // Body
        ctx.beginPath();
        ctx.moveTo(x, y - 40*scale);
        ctx.lineTo(x, y - 20*scale);
        ctx.stroke();

        // Arms
        ctx.beginPath();
        ctx.moveTo(x, y - 35*scale);
        ctx.lineTo(x + (15*scale * facing), y - 25*scale); // Front arm
        ctx.moveTo(x, y - 35*scale);
        ctx.lineTo(x - (10*scale * facing), y - 25*scale); // Back arm
        ctx.stroke();

        // Legs
        ctx.beginPath();
        ctx.moveTo(x, y - 20*scale);
        ctx.lineTo(x + (10*scale * facing), y); // Front leg
        ctx.moveTo(x, y - 20*scale);
        ctx.lineTo(x - (10*scale * facing), y); // Back leg
        ctx.stroke();
    }

    function drawWalk() {
        const width = walkCanvas.offsetWidth;
        const height = walkCanvas.offsetHeight;
        
        const { axisY, unit } = drawGrid(ctxWalk, width, height, false);

        // Draw Stick Figure
        const x = getX(state.position, width);
        drawStickFigure(ctxWalk, x, axisY, state.facing);
    }

    function drawDistribution() {
        const width = distCanvas.offsetWidth;
        const height = distCanvas.offsetHeight;
        
        const { axisY, unit } = drawGrid(ctxDist, width, height, true);

        // Find max probability to scale Y axis
        let maxProb = 0;
        for (const p of Object.values(state.probabilities)) {
            if (p > maxProb) maxProb = p;
        }
        if (maxProb === 0) maxProb = 1;

        // Draw Bars
        const barWidth = unit * 0.6;
        const maxBarHeight = height - 50; // Leave room for axis

        ctxDist.fillStyle = 'rgba(16, 185, 129, 0.6)'; // Green
        ctxDist.strokeStyle = 'rgba(16, 185, 129, 1)';

        for (const [posStr, prob] of Object.entries(state.probabilities)) {
            const pos = parseInt(posStr);
            if (pos < -state.viewRange || pos > state.viewRange) continue;

            const x = getX(pos, width);
            const barHeight = (prob / maxProb) * maxBarHeight;
            
            ctxDist.fillRect(x - barWidth/2, axisY - barHeight, barWidth, barHeight);
            ctxDist.strokeRect(x - barWidth/2, axisY - barHeight, barWidth, barHeight);
        }
    }

    function drawAll() {
        drawWalk();
        drawDistribution();
    }

    // Start
    init();

</script>

</body>
</html>
