import { mergeSort } from '../MergeSort';

describe('Merge Sort', () => {
  it('should sort array correctly', () => {
    const initialState = [1, 3, 2, 5, 6, 2, 4, 2, 3];
    const expectedState = [...initialState].sort();

    mergeSort(initialState);

    expect(initialState).toEqual(expectedState);
  });

  it('should sort an array with random values correctly', () => {
    const array = [...Array(100)].map(_ => Math.floor(Math.random() * 100));
    const expected = [...array].sort((a, b) => a - b);

    mergeSort(array);

    expect(array).toEqual(expected);
  });
});
