import { bubbleSort } from '../BubbleSort';

describe('Bubble Sort', () => {
  it('should sort array correctly', () => {
    const initialState = [1, 3, 2, 5, 4, 6, 2, 4, 8];
    const expectedState = [...initialState].sort();

    bubbleSort(initialState);

    expect(initialState).toEqual(expectedState);
  });
});
