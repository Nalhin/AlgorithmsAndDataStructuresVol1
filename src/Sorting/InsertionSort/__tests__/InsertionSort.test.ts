import { insertionSort } from '../InsertionSort';

describe('Insertion Sort', () => {
  it('should sort array correctly', () => {
    const initialState = [1, 3, 2, 5, 4, 6, 2, 4, 8];
    const expectedState = [...initialState].sort();

    insertionSort(initialState);

    expect(initialState).toEqual(expectedState);
  });
});
