import { selectionSort } from '../SelectionSort';

describe('Selection Sort', () => {
  it('should sort array correctly', () => {
    const initialState = [1, 3, 2, 5, 4, 6, 2, 4, 8];
    const expectedState = [...initialState].sort();

    selectionSort(initialState);

    expect(initialState).toEqual(expectedState);
  });
});
