export function heapSort(array: number[]): void {
  buildMaxHeap(array);

  for (let i = array.length - 1; i >= 0; i--) {
    [array[0], array[i]] = [array[i], array[0]];
    maxHeapify(array, 0, i);
  }
}

export function buildMaxHeap(array: number[]): void {
  for (let i = Math.floor(array.length / 2) - 1; i >= 0; i--) {
    maxHeapify(array, i, array.length);
  }
}

function maxHeapify(array: number[], i: number, heapSize: number): void {
  while (i !== heapSize) {
    const left = getLeftPosition(i);
    const right = getRightPosition(i);
    let largest = i;
    if (left < heapSize && array[left] > array[largest]) {
      largest = left;
    }
    if (right < heapSize && array[right] > array[largest]) {
      largest = right;
    }

    if (largest === i) {
      return;
    }

    [array[i], array[largest]] = [array[largest], array[i]];
    maxHeapify(array, largest, heapSize);
  }
}

function getLeftPosition(i: number): number {
  return i * 2 + 1;
}

function getRightPosition(i: number): number {
  return i * 2 + 2;
}
