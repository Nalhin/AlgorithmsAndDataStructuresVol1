import { mergeSort } from '../MergeSort';

describe('Merge Sort', () => {
  it('should sort array correctly', () => {
    const initialState = [1, 3, 2, 5, 6, 2, 4, 2, 3];
    const expectedState = [...initialState].sort();

    mergeSort(initialState);

    expect(initialState).toEqual(expectedState);
  });
});
