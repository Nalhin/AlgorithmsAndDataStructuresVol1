export function maximumSubarrayKadane(array: number[]) {
  let bestStart = null;
  let bestEnd = null;
  let bestSum = -Infinity;

  let currentSum = 0;
  let currentStart = 0;

  for (let i = 0; i < array.length; i++) {
    currentSum += array[i];
    if (currentSum > bestSum) {
      bestSum = currentSum;
      bestEnd = i;
      bestStart = currentStart;
    }
    if (currentSum < 0) {
      currentSum = 0;
      currentStart = i + 1;
    }
  }
  return array.slice(bestStart, bestEnd + 1);
}
