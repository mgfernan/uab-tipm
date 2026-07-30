class Satellite {
  constructor(x, y) {
    this.x = x;
    this.y = y;
    this.angle = 0; // optional
  }

  draw(p) {
    p.push();
    p.translate(this.x, this.y);
    p.rotate(this.angle ?? 0);
    p.rectMode(p.CENTER);

    // Main body
    p.stroke(255, 209, 102);
    p.fill(255, 209, 102);
    p.rect(0, 0, 18, 12, 3);

    // Solar panels / wings
    p.fill(180, 220, 255);
    p.rect(-18, 0, 16, 7, 2);
    p.rect(18, 0, 16, 7, 2);

    p.pop();
  }
}

class BeamCone {
  constructor({ earthY, originX, originY, angleDeg = 25, maxAngleDeg = 70 }) {
    this.earthY = earthY;
    this.originX = originX;
    this.originY = originY;
    this.angleDeg = angleDeg;
    this.maxAngleDeg = maxAngleDeg;
  }

  setAngleDeg(deg) {
    this.angleDeg = Math.max(0, Math.min(this.maxAngleDeg, deg));
  }

  getFootprintWidthPx(p) {
    const heightToEarth = this.earthY - this.originY;
    if (heightToEarth <= 0) return 0;

    const angleRad = p.radians(this.angleDeg);
    const halfWidth = Math.tan(angleRad) * heightToEarth;
    const width = 2 * halfWidth;

    return p.constrain(width, 0, p.width);
  }

  getFootprintWidthKm(p) {
    const heightToEarthKm = 36000;
    const angleRad = p.radians(this.angleDeg);
    const halfWidthKm = Math.tan(angleRad) * heightToEarthKm;
    return 2 * halfWidthKm;
  }

  draw(p) {
    const widthOnEarth = this.getFootprintWidthPx(p);
    const leftX = this.originX - widthOnEarth / 2;
    const rightX = this.originX + widthOnEarth / 2;

    // Beam footprint
    p.push();
    p.noStroke();
    p.fill(255, 220, 80, 140);
    p.rect(leftX, this.earthY, widthOnEarth, p.height - this.earthY);

    // Outline
    p.stroke(255, 200, 60, 200);
    p.noFill();
    p.rect(leftX, this.earthY, widthOnEarth, 1);

    // Wedge edges
    p.stroke(255, 200, 60, 220);
    p.line(this.originX, this.originY, leftX, this.earthY);
    p.line(this.originX, this.originY, rightX, this.earthY);

    // Numbers (below slider)
    p.noStroke();
    p.fill(237, 242, 255, 220);
    p.textSize(13);
    p.textAlign(p.LEFT, p.TOP);

    p.text(`Beam angle: ${this.angleDeg.toFixed(1)}°`, 12, 55);
    p.text(`Beam width on Earth: ${this.getFootprintWidthKm(p).toFixed(1)} km`, 12, 75);

    p.pop();
  }
}

function drawEarthSceneCore(p, state, opts = {}) {
  const earthY = p.height * 0.78;

  // Create objects once
  if (!state.satellite || !state.beam) {
    const originX = p.width / 2;
    const originY = earthY - 220;

    state.satellite = new Satellite(originX, originY);
    state.beam = new BeamCone({
      earthY,
      originX,
      originY,
      angleDeg: 25,
      maxAngleDeg: 70
    });
  }

  // Update layout
  const originX = p.width / 2;
  const originY = earthY - 220;

  state.satellite.x = originX;
  state.satellite.y = originY;

  state.beam.earthY = earthY;
  state.beam.originX = originX;
  state.beam.originY = originY;

  // Slider -> beam angle
  if (state.angleSlider) state.beam.setAngleDeg(state.angleSlider.value());

  // Earth background / grid (your snippet)
  p.noStroke();
  p.fill(20, 34, 69);
  p.rect(0, 0, p.width, p.height, 14);

  for (let i = 0; i < 10; i++) {
    p.stroke(255, 255, 255, 18);
    p.line((i / 9) * p.width, 0, (i / 9) * p.width, p.height);
  }

  for (let i = 0; i < 6; i++) {
    p.noStroke();
    p.stroke(255, 255, 255, 25);
    p.line(0, (i / 5) * p.height, p.width, (i / 5) * p.height);
  }

  p.noStroke();
  p.fill(58, 123, 213);
  p.rect(0, earthY, p.width, p.height - earthY);

  // Satellite + beam
  state.satellite.draw(p);
  state.beam.draw(p);

  // Label on top (above slider)
  if (opts.label) {
    p.push();
    p.noStroke();
    p.fill(237, 242, 255, 220);
    p.textSize(13);
    p.textAlign(p.LEFT, p.TOP);
    p.text(opts.label, 12, 0); // <-- above slider
    p.pop();
  }
}

// ---- p5 sketch you can paste into editor.p5js.org ----
let sketchState = {};

let geoSketch = (p) => {
  p.setup = () => {
    p.createCanvas(900, 600);

    sketchState.angleSlider = p.createSlider(1, 18, 25, 0.5);
    sketchState.angleSlider.position(20, 20);
    sketchState.angleSlider.style("width", "220px");
  };

  p.draw = () => {
    p.clear();
    drawEarthSceneCore(p, sketchState, {
      label: "GEO (fixed-beam): Coverage anchored to an Earth region"
    });
  };
};

window.addEventListener("DOMContentLoaded", () => {
  const geo = document.getElementById("sketch-geo");
  if (!geo) {
    console.error("Missing container: #sketch-geo");
    return;
  }

  let state = {}; // state must be instance-specific

  const sketch = (p) => {
    p.setup = () => {
      p.createCanvas(900, 600).parent(geo);

      state.angleSlider = p.createSlider(1, 18, 25, 0.5);
      state.angleSlider.position(20, 20);
      state.angleSlider.style("width", "220px");
    };

    p.draw = () => {
      p.clear();
      drawEarthSceneCore(p, state, {
        label: "GEO (fixed-beam): Coverage anchored to an Earth region"
      });
    };
  };

  new p5(sketch);
});
