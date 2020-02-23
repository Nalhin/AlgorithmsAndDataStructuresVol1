interface MaximumSubarray {
  start: number;
  end: number;
  sum: number;
}

export function maximumSubarrayDivideAndConquer(array: number[], startIndex = 0, endIndex = array.length - 1): MaximumSubarray {

  if (endIndex===startIndex) {
    return { start: startIndex, end: endIndex, sum: array[startIndex] };
  }

  const middleIndex = Math.floor((startIndex + endIndex) / 2);

  const leftSubarray = maximumSubarrayDivideAndConquer(array, startIndex, middleIndex);
  const rightSubarray = maximumSubarrayDivideAndConquer(array, middleIndex + 1, endIndex);
  const middleSubarray = findMaximumCrossingSubarray(array, startIndex, middleIndex, endIndex);

  if (leftSubarray.sum >= rightSubarray.sum && leftSubarray.sum >= middleSubarray.sum) {
    return leftSubarray;
  }
  if (rightSubarray.sum >= leftSubarray.sum && rightSubarray.sum >= middleSubarray.sum) {
    return rightSubarray;
  }
  return middleSubarray;
}

function findMaximumCrossingSubarray(array: number[], startIndex: number, middleIndex: number, endIndex: number): MaximumSubarray {
  let leftSum = -Infinity;
  let sum = 0;
  let maxLeftIndex = 0;

  for (let i = middleIndex; i >= 0; i--) {
    sum += array[i];
    if (sum > leftSum) {
      leftSum = sum;
      maxLeftIndex = i;
    }
  }

  sum = 0;
  let rightSum = -Infinity;
  let maxRightIndex = 0;

  for (let i = middleIndex + 1; i <= endIndex; i++) {
    sum += array[i];
    if (sum > rightSum) {
      rightSum = sum;
      maxRightIndex = i;
    }
  }

  return {
    start: maxLeftIndex,
    end: maxRightIndex,
    sum: leftSum + rightSum,
  };
}