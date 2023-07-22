//Pearson Correlation

function pearson(values) {
  const n = values.length;

  if (n == 0) return 0;

  let meanX = 0;
  let meanY = 0;
  for (var i = 0; i < n; i++) {
    meanX += values[i].x / n;
    meanY += values[i].y / n;
  }

  let num = 0;
  let den1 = 0;
  let den2 = 0;

  for (var i = 0; i < n; i++) {
    let dx = values[i].x - meanX;
    let dy = values[i].y - meanY;
    num += dx * dy;
    den1 += dx * dx;
    den2 += dy * dy;
  }

  const den = Math.sqrt(den1) * Math.sqrt(den2);

  if (den == 0) return 0;

  return num / den;
}

pearson([
  { x: 0, y: 0 },
  { x: 1, y: 1 },
]);
