/**
 * Sorts given array in place with merge sort algorithm.
 *
 * @param {number[]} array - array to sort
 * @param {number=} startIndex - index from which to start sorting
 * @param {number=} endIndex - index from which to end sorting
 */
export function mergeSortArray(array: number[], startIndex = 0, endIndex = array.length - 1) {
  if (startIndex < endIndex) {
    const middleIndex = Math.floor((startIndex + endIndex) / 2);
    mergeSortArray(array, startIndex, middleIndex);
    mergeSortArray(array, middleIndex + 1, endIndex);
    mergeArray(array, startIndex, middleIndex, endIndex);
  }
}

/**
 * Merges two sorted arrays in place
 * @param array - array to merge
 * @param startIndex - index of the first element in sorted left slice
 * @param middleIndex - index of the last element in sorted left slice
 * @param endIndex - index of the last element in sorted right slice
 */
function mergeArray(
  array: number[],
  startIndex: number,
  middleIndex: number,
  endIndex: number,
) {
  // slice not inclusive
  const leftSlice = array.slice(startIndex, middleIndex + 1);
  const rightSlice = array.slice(middleIndex + 1, endIndex + 1);

  let leftSliceIndex = 0;
  let rightSliceIndex = 0;
  let mergedIndex = startIndex;

  while (leftSliceIndex < leftSlice.length && rightSliceIndex < rightSlice.length) {
    if (leftSlice[leftSliceIndex ] <= rightSlice[rightSliceIndex]) {
      array[mergedIndex] = leftSlice[leftSliceIndex];
      leftSliceIndex++;
    } else {
      array[mergedIndex] = rightSlice[rightSliceIndex];
      rightSliceIndex++;
    }
    mergedIndex++;
  }

  while (rightSliceIndex < rightSlice.length) {
    array[mergedIndex] = rightSlice[rightSliceIndex];
    mergedIndex++;
    rightSliceIndex++;
  }

  while (leftSliceIndex < leftSlice.length) {
    array[mergedIndex] = leftSlice[leftSliceIndex];
    mergedIndex++;
    leftSliceIndex++;
  }
}
