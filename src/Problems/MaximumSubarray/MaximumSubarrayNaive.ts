export function maximumSubarrayNaive(array: number[]) {
  let maxSum = -Infinity;
  let maxStart: number;
  let maxEnd: number;

  for (let i = 0; i < array.length; i++) {
    let sum = 0;
    for (let j = i; j < array.length; j++) {
      sum += array[j];
      if (sum >= maxSum) {
        maxSum = sum;
        maxEnd = j;
        maxStart = i;
      }
    }
  }

  return array.slice(maxStart, maxEnd + 1);
}
