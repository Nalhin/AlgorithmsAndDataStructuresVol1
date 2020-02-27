interface MaximumSubarray {
  start: number;
  end: number;
  sum: number;
}

export function maximumSubarrayDivideAndConquer(array: number[]) {
  const solution = maximumSubarrayRecursive(array, 0, array.length - 1);
  return array.slice(solution.start, solution.end + 1);
}

function maximumSubarrayRecursive(
  array: number[],
  startIndex: number,
  endIndex: number,
): MaximumSubarray {
  if (endIndex === startIndex) {
    return { start: startIndex, end: endIndex, sum: array[startIndex] };
  }

  const middleIndex = Math.floor((startIndex + endIndex) / 2);

  const leftSubarray = maximumSubarrayRecursive(array, startIndex, middleIndex);
  const rightSubarray = maximumSubarrayRecursive(
    array,
    middleIndex + 1,
    endIndex,
  );
  const middleSubarray = findMaximumCrossingSubarray(
    array,
    startIndex,
    middleIndex,
    endIndex,
  );

  return returnMaximumSubarray(leftSubarray, rightSubarray, middleSubarray);
}

function returnMaximumSubarray(...subArrays) {
  return subArrays.reduce((prev, curr) => (prev.sum > curr.sum ? prev : curr));
}

function findMaximumCrossingSubarray(
  array: number[],
  startIndex: number,
  middleIndex: number,
  endIndex: number,
): MaximumSubarray {
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
