export function selectionSort(array: number[]) {
  for (let i = 0; i < array.length; i++) {
    const smallest = findIndexOfSmallestElement(array, i);
    [array[i], array[smallest]] = [array[smallest], array[i]];
  }
}

function findIndexOfSmallestElement(array: number[], initialIndex: number) {
  let smallestIndex = initialIndex;

  for (let i = initialIndex + 1; i < array.length; i++) {
    if (array[i] < array[smallestIndex]) {
      smallestIndex = i;
    }
  }

  return smallestIndex;
}
