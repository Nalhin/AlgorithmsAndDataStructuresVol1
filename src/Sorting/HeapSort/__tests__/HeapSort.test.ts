import { buildMaxHeap, heapSort } from '../HeapSort';

describe('Heap Sort', () => {
  it('should build max heap', () => {
    const initialState = [5, 13, 2, 25, 7, 17, 20, 8, 4];
    const expectedState = [25, 13, 20, 8, 7, 17, 2, 5, 4];

    buildMaxHeap(initialState);

    expect(initialState).toEqual(expectedState);
  });

  it('should sort an array correctly', () => {
    const array = [1, 3, 2, 5, 6, 2, 4, 2, 3, 8];
    const expected = [...array].sort((a, b) => a - b);

    heapSort(array);

    expect(array).toEqual(expected);
  });

  it('should sort an array with random values correctly', () => {
    const array = [...Array(100)].map((_) => Math.floor(Math.random() * 100));
    const expected = [...array].sort((a, b) => a - b);

    heapSort(array);

    expect(array).toEqual(expected);
  });
});
