import { quickSort } from '../QuickSort';

describe('Quick Sort', () => {
  it('should sort an array correctly', () => {
    const initialState = [1, 3, 2, 5, 4, 6, 2, 4, 8];
    const expectedState = [...initialState].sort((a, b) => a - b);

    quickSort(initialState);

    expect(initialState).toEqual(expectedState);
  });

  it('should sort an array with random values correctly', () => {
    const array = [...Array(100)].map(_ => Math.floor(Math.random() * 100));
    const expected = [...array].sort((a, b) => a - b);

    quickSort(array);

    expect(array).toEqual(expected);
  });
});
