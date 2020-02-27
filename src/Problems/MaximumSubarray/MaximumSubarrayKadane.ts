interface MaximumSubarray {
  start: number;
  end: number;
  sum: number;
}

export function maximumSubarrayKadane(array: number[]) {
  const maximumSubarray: MaximumSubarray = {
    start: null,
    end: null,
    sum: -Infinity,
  };

  let currentSum = 0;
  let currentStart = 0;
  for (let i = 0; i < array.length; i++) {
    currentSum += array[i];
    if (currentSum > maximumSubarray.sum) {
      maximumSubarray.sum = currentSum;
      maximumSubarray.end = i;
      maximumSubarray.start = currentStart;
    }
    if (currentSum < 0) {
      currentSum = 0;
      currentStart = i + 1;
    }
  }
  return array.slice(maximumSubarray.start, maximumSubarray.end + 1);
}
