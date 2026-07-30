const sketches = [];
let running = true;

function registerSketch(instance, name) {
    instance._exportName = name;
    sketches.push(instance);
}

function drawEarthScene(p, opts = {}) {
    const earthY = p.height * 0.78;
    p.noStroke();
    p.fill(20, 34, 69);
    p.rect(0, 0, p.width, p.height, 14);

    for (let i = 0; i < 10; i++) {
    p.stroke(255, 255, 255, 18);
    p.line((i / 9) * p.width, 0, (i / 9) * p.width, p.height);
    }
    for (let i = 0; i < 6; i++) {
    p.line(0, (i / 5) * p.height, p.width, (i / 5) * p.height);
    }

    p.noStroke();
    p.fill(58, 123, 213);
    p.rect(0, earthY, p.width, p.height - earthY);

    p.fill(101, 193, 140);
    p.beginShape();
    p.vertex(0, earthY + 14);
    p.bezierVertex(24, earthY - 10, 52, earthY + 16, 86, earthY + 5);
    p.bezierVertex(120, earthY - 7, 150, earthY + 10, 180, earthY + 4);
    p.bezierVertex(205, earthY + 2, 226, earthY + 18, 252, earthY + 8);
    p.vertex(252, p.height);
    p.vertex(0, p.height);
    p.endShape(p.CLOSE);

    if (opts.label) {
    p.fill(237, 242, 255, 220);
    p.textSize(13);
    p.textAlign(p.LEFT, p.TOP);
    p.text(opts.label, 12, 12);
    }
    return earthY;
}

function drawSatellite(p, x, y, angle = 0) {
    p.push();
    p.translate(x, y);
    p.rotate(angle);
    p.rectMode(p.CENTER);
    p.stroke(255, 209, 102);
    p.fill(255, 209, 102);
    p.rect(0, 0, 18, 12, 3);
    p.fill(180, 220, 255);
    p.rect(-18, 0, 16, 7, 2);
    p.rect(18, 0, 16, 7, 2);
    p.pop();
}

function beamCone(p, satX, satY, leftX, rightX, groundY, fillColor, edgeColor) {
    p.noStroke();
    p.fill(fillColor);
    p.beginShape();
    p.vertex(satX, satY + 4);
    p.vertex(rightX, groundY);
    p.vertex(leftX, groundY);
    p.endShape(p.CLOSE);
    p.stroke(edgeColor);
    p.strokeWeight(1.5);
    p.line(satX, satY + 4, leftX, groundY);
    p.line(satX, satY + 4, rightX, groundY);
}

const geoSketch = (p) => {
    let t = 0;
    p.setup = () => {
    const c = p.createCanvas(320, 240);
    c.parent('sketch-geo');
    registerSketch(p, 'fixed-beam-geo');
    };
    p.draw = () => {
    t += running ? 0.02 : 0;
    const groundY = drawEarthScene(p, { label: 'Coverage anchored to one Earth region' });
    const satX = p.width * 0.5;
    const satY = 46;
    const wobble = Math.sin(t) * 1.2;
    const left = p.width * 0.33;
    const right = p.width * 0.67;
    beamCone(p, satX + wobble, satY, left, right, groundY, 'rgba(84,227,255,0.20)', 'rgba(84,227,255,0.92)');
    p.noStroke();
    p.fill(84, 227, 255, 45);
    p.ellipse((left + right) / 2, groundY, right - left, 26);
    p.stroke(124, 242, 154);
    p.strokeWeight(2);
    p.line((left + right) / 2, groundY - 20, (left + right) / 2, groundY + 14);
    p.line((left + right) / 2 - 17, groundY - 3, (left + right) / 2 + 17, groundY - 3);
    drawSatellite(p, satX, satY, 0);
    p.noStroke();
    p.fill(237, 242, 255);
    p.textSize(12);
    p.textAlign(p.CENTER);
    p.text('GEO platform\nno apparent orbital sweep', satX, 72);
    };
};

const quasiSketch = (p) => {
    let phase = 0;
    p.setup = () => {
    const c = p.createCanvas(320, 240);
    c.parent('sketch-quasi');
    registerSketch(p, 'quasi-fixed-earth-beam-leo');
    };
    p.draw = () => {
    phase += running ? 0.015 : 0;
    const groundY = drawEarthScene(p, { label: 'Beam stays on one cell while satellite moves' });
    const startX = 66;
    const endX = 250;
    const satX = p.map((Math.sin(phase) + 1) / 2, 0, 1, startX, endX);
    const satY = 54 + Math.cos(phase * 1.1) * 8;
    const cellX = p.width * 0.58;
    const cellW = 54;

    p.noFill();
    p.stroke(255, 209, 102, 90);
    p.strokeWeight(2);
    p.arc(p.width / 2, 96, 220, 88, p.PI, p.TWO_PI);

    p.noStroke();
    p.fill(124, 242, 154, 50);
    p.ellipse(cellX, groundY, cellW, 24);
    p.stroke(124, 242, 154);
    p.strokeWeight(2);
    p.rectMode(p.CENTER);
    p.rect(cellX, groundY - 4, cellW, 16, 4);

    beamCone(p, satX, satY, cellX - cellW / 2, cellX + cellW / 2, groundY, 'rgba(124,242,154,0.15)', 'rgba(124,242,154,0.95)');
    drawSatellite(p, satX, satY, 0.15);

    p.noStroke();
    p.fill(237, 242, 255);
    p.textSize(12);
    p.textAlign(p.LEFT);
    p.text('short dwell / tracking mode', 14, 32);
    p.textAlign(p.CENTER);
    p.text('ground cell held quasi-fixed', cellX, groundY - 24);
    };
};

const movingSketch = (p) => {
    let phase = 0;
    p.setup = () => {
    const c = p.createCanvas(320, 240);
    c.parent('sketch-moving');
    registerSketch(p, 'moving-beam-leo');
    };
    p.draw = () => {
    phase += running ? 0.018 : 0;
    const groundY = drawEarthScene(p, { label: 'Footprint travels with the satellite' });
    const u = (Math.sin(phase) + 1) / 2;
    const satX = p.lerp(54, 266, u);
    const satY = 58 - Math.sin(phase * 2) * 4;
    const beamCenter = p.lerp(36, 284, u);
    const beamWidth = 56;

    p.noFill();
    p.stroke(255, 209, 102, 70);
    p.strokeWeight(2);
    p.arc(p.width / 2, 102, 244, 92, p.PI, p.TWO_PI);

    beamCone(p, satX, satY, beamCenter - beamWidth / 2, beamCenter + beamWidth / 2, groundY, 'rgba(255,143,171,0.16)', 'rgba(255,143,171,0.92)');
    p.noStroke();
    p.fill(255, 143, 171, 60);
    p.ellipse(beamCenter, groundY, beamWidth, 22);

    for (let i = 0; i < 4; i++) {
        const trailX = beamCenter - i * 34;
        if (trailX > 0) {
        p.fill(255, 143, 171, Math.max(0, 52 - i * 12));
        p.ellipse(trailX, groundY, beamWidth - i * 6, 16 - i * 2);
        }
    }

    drawSatellite(p, satX, satY, 0.1);
    p.noStroke();
    p.fill(237, 242, 255);
    p.textSize(12);
    p.textAlign(p.CENTER);
    p.text('coverage sweep direction →', p.width * 0.58, 28);
    };
};

const steeringSketch = (p) => {
    let phase = 0;
    const users = [0.24, 0.47, 0.72];
    p.setup = () => {
    const c = p.createCanvas(320, 240);
    c.parent('sketch-steering');
    registerSketch(p, 'beam-steering-leo');
    };
    p.draw = () => {
    phase += running ? 0.02 : 0;
    const groundY = drawEarthScene(p, { label: 'Electronic steering retargets different cells' });
    const satX = 164 + Math.sin(phase * 0.45) * 28;
    const satY = 52;
    const idx = Math.floor((phase / 1.6) % users.length);
    const nextIdx = (idx + 1) % users.length;
    const blend = (phase % 1.6) / 1.6;
    const targetX = p.lerp(users[idx] * p.width, users[nextIdx] * p.width, blend);
    const spread = 24;

    users.forEach((u, i) => {
        const x = u * p.width;
        p.noStroke();
        p.fill(i === idx ? 'rgba(197,155,255,0.35)' : 'rgba(255,255,255,0.10)');
        p.ellipse(x, groundY, 28, 18);
        p.fill(237, 242, 255);
        p.circle(x, groundY - 10, 5);
    });

    beamCone(p, satX, satY, targetX - spread, targetX + spread, groundY, 'rgba(197,155,255,0.16)', 'rgba(197,155,255,0.95)');
    drawSatellite(p, satX, satY, 0);

    p.stroke(197, 155, 255, 120);
    p.strokeWeight(1);
    for (const u of users) p.line(satX, satY + 3, u * p.width, groundY - 8);

    p.noStroke();
    p.fill(237, 242, 255);
    p.textSize(12);
    p.textAlign(p.CENTER);
    p.text('beam hops between users/cells', p.width / 2, 28);
    };
};
/*
new p5(geoSketch, 'sketch-geo');
new p5(quasiSketch, 'sketch-quasi');
new p5(movingSketch, 'sketch-moving');
new p5(steeringSketch, 'sketch-steering');

document.getElementById('toggleAnim').addEventListener('click', () => {
    running = !running;
    document.getElementById('toggleAnim').textContent = running ? 'Pause animations' : 'Resume animations';
});

document.getElementById('saveAll').addEventListener('click', () => {
    sketches.forEach((s, i) => setTimeout(() => s.saveCanvas(s._exportName, 'png'), i * 180));
});
*/

window.addEventListener("DOMContentLoaded", () => {
  const quasi = document.getElementById("sketch-quasi");
  const moving = document.getElementById("sketch-moving");
  const steering = document.getElementById("sketch-steering");

  if (quasi) new p5(quasiSketch, quasi);
  if (moving) new p5(movingSketch, moving);
  if (steering) new p5(steeringSketch, steering);
});