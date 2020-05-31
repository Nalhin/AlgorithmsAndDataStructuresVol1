import { LRUChache } from '../LruCache';

describe('LRUCache', () => {
  let lruCache: LRUChache;

  beforeEach(() => {
    lruCache = new LRUChache(2);
  });

  it('should put and get item correctly', () => {
    const item = {
      key: 1,
      value: 2,
    };

    lruCache.put(item.key, item.value);
    const result = lruCache.get(item.key);

    expect(result).toBe(item.value);
  });

  it('should correctly execute operations in the following order', () => {
    const expected = [-1, -1, 2, 6];
    const result = [];

    result.push(lruCache.get(2));
    lruCache.put(2, 6);
    result.push(lruCache.get(1));
    lruCache.put(1, 5);
    lruCache.put(1, 2);
    result.push(lruCache.get(1));
    result.push(lruCache.get(2));

    expect(result).toEqual(expected);
  });
});
