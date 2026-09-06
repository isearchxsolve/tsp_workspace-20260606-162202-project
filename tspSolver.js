function tspSolver(graph) {
  // Note: The Travelling Salesman Problem is NP-hard and cannot be solved in O(n) time complexity.
  // The following is a nearest neighbor approximation algorithm, which has a time complexity of O(n^2).
  const numCities = graph.length;
  const visited = new Array(numCities).fill(false);
  const path = [];
  let currentCity = 0;
  visited[currentCity] = true;
  path.push(currentCity);

  for (let i = 0; i < numCities - 1; i++) {
    let minDistance = Infinity;
    let nextCity = -1;
    for (let j = 0; j < numCities; j++) {
      if (!visited[j] && graph[currentCity][j] < minDistance) {
        minDistance = graph[currentCity][j];
        nextCity = j;
      }
    }
    visited[nextCity] = true;
    path.push(nextCity);
    currentCity = nextCity;
  }

  return path;
}

module.exports = tspSolver;
